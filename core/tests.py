from django.test import TestCase
from django.urls import reverse


class HostPwaTests(TestCase):
    def test_host_page_has_separate_installable_pwa_hooks(self):
        response = self.client.get(reverse('host'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'rel="manifest"')
        self.assertContains(response, 'href="/host/manifest.json"')
        self.assertContains(response, 'serviceWorker.register')
        self.assertContains(response, '/host/sw.js')
        self.assertContains(response, 'نسخه مخصوص این صفحه')

    def test_host_manifest_and_service_worker_endpoints(self):
        manifest_response = self.client.get(reverse('host_manifest'))
        self.assertEqual(manifest_response.status_code, 200)
        self.assertEqual(manifest_response['Content-Type'], 'application/manifest+json')
        self.assertContains(manifest_response, '"start_url": "/host/"')
        self.assertContains(manifest_response, '"scope": "/host/"')

        service_worker_response = self.client.get(reverse('host_service_worker'))
        self.assertEqual(service_worker_response.status_code, 200)
        self.assertEqual(service_worker_response['Content-Type'], 'application/javascript')
        self.assertContains(service_worker_response, 'self.addEventListener')
        self.assertContains(service_worker_response, '/host/')

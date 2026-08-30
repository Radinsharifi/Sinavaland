from django.test import TestCase
from django.urls import reverse


class PersianSlugUrlTests(TestCase):
    def test_persian_slug_is_supported_in_reverse(self):
        url = reverse('accommodations:detail', kwargs={'slug': 'هتل-کاخ-نیاوران'})
        self.assertEqual(url, '/accommodations/%D9%87%D8%AA%D9%84-%DA%A9%D8%A7%D8%AE-%D9%86%DB%8C%D8%A7%D9%88%D8%B1%D8%A7%D9%86/')

        url = reverse('magazine:detail', kwargs={'slug': 'مقاله-سفر-به-شیراز'})
        self.assertEqual(url, '/magazine/%D9%85%D9%82%D8%A7%D9%84%D9%87-%D8%B3%D9%81%D8%B1-%D8%A8%D9%87-%D8%B4%DB%8C%D8%B1%D8%A7%D8%B2/')


class HostPwaTests(TestCase):
    def test_host_page_has_separate_installable_pwa_hooks(self):
        response = self.client.get(reverse('core:host'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'rel="manifest"')
        self.assertContains(response, 'href="/host/manifest.json"')
        self.assertContains(response, 'serviceWorker.register')
        self.assertContains(response, '/host/sw.js')
        self.assertContains(response, 'نسخه مخصوص این صفحه')

    def test_host_manifest_and_service_worker_endpoints(self):
        manifest_response = self.client.get(reverse('core:host_manifest'))
        self.assertEqual(manifest_response.status_code, 200)
        self.assertEqual(manifest_response['Content-Type'], 'application/manifest+json')
        self.assertContains(manifest_response, '"start_url": "/host/"')
        self.assertContains(manifest_response, '"scope": "/host/"')

        service_worker_response = self.client.get(reverse('core:host_service_worker'))
        self.assertEqual(service_worker_response.status_code, 200)
        self.assertEqual(service_worker_response['Content-Type'], 'application/javascript')
        self.assertContains(service_worker_response, 'self.addEventListener')
        self.assertContains(service_worker_response, '/host/')

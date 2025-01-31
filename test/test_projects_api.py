# coding: utf-8

"""
    Patch API V1

    The core API used to integrate with Patch's service  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: developers@usepatch.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import os

from patch_api.api_client import ApiClient


class TestProjectsApi(unittest.TestCase):
    """ProjectsApi unit test stubs"""

    def setUp(self):
        api_client = ApiClient(api_key=os.environ.get("SANDBOX_API_KEY"))
        self.api = api_client.projects  # noqa: E501

    def tearDown(self):
        self.api = None

    def test_retrieve_project(self):
        """Test case for retrieve_project

        Retrieves a project  # noqa: E501
        """
        project_id = "pro_test_2b67b11a030b66e0a6dd61a56b49079a"
        project = self.api.retrieve_project(id=project_id).data
        self.assertTrue(project)
        self.assertEqual(project.production, False)
        self.assertTrue(isinstance(project.photos, list))

        self.assertTrue(hasattr(project, "tagline"))
        self.assertTrue(hasattr(project, "latitude"))
        self.assertTrue(hasattr(project, "longitude"))
        self.assertTrue(hasattr(project, "highlights"))

        self.assertTrue(isinstance(project.mechanism, str))
        self.assertTrue(isinstance(project.state, str))

        technology_type = project.technology_type
        self.assertTrue(isinstance(technology_type.name, str))
        self.assertTrue(isinstance(technology_type.slug, str))

        parent_technology_type = technology_type.parent_technology_type
        self.assertTrue(isinstance(parent_technology_type.name, str))
        self.assertTrue(isinstance(parent_technology_type.slug, str))

    def test_retrieve_projects(self):
        """Test case for retrieve_projects

        Retrieves a list of projects  # noqa: E501
        """
        projects = self.api.retrieve_projects().data
        self.assertTrue(isinstance(projects, list))

        if len(projects) > 0:
            project = projects[0]

            self.assertEqual(project.production, False)
            self.assertGreater(project.average_price_per_tonne_cents_usd, 0)
            self.assertGreater(project.remaining_mass_g, 0)
            self.assertEqual(project.standard, None)
            self.assertIsInstance(project.name, str)
            self.assertTrue(project.description)
            self.assertIsInstance(project.country, str)
            self.assertIsInstance(project.type, str)
            self.assertIsInstance(project.developer, str)
            self.assertTrue(isinstance(project.photos, list))

    def test_retrieve_biomass_projects(self):
        """Test case for retrieve_projects with a type filter

        Retrieves a list of projects  # noqa: E501
        """
        project_type = "biomass"
        projects = self.api.retrieve_projects(type=project_type).data
        self.assertTrue(isinstance(projects, list))

        for project in projects:
            self.assertEqual(project.type, project_type)

    def test_retrieve_american_projects(self):
        """Test case for retrieve_projects with a country filter

        Retrieves a list of projects  # noqa: E501
        """
        project_country = "US"
        projects = self.api.retrieve_projects(country=project_country).data
        self.assertTrue(isinstance(projects, list))

        for project in projects:
            self.assertEqual(project.country, project_country)

    def test_retrieve_projects_with_more_than_100_grams_of_inventory(self):
        """Test case for retrieve_projects with a country filter

        Retrieves a list of projects  # noqa: E501
        """
        minimum_available_mass = 100
        projects = self.api.retrieve_projects(
            minimum_available_mass=minimum_available_mass
        ).data
        self.assertTrue(isinstance(projects, list))

        for project in projects:
            self.assertTrue(project.remaining_mass_g >= minimum_available_mass)


if __name__ == "__main__":
    unittest.main()

from django.test import TestCase
from ong.models import Ong

from subsidy.models import Subsidy

# Create your tests here.


class SubsidyTestCase(TestCase):
    def setUp(self):
        self.ong = Ong.objects.create(name='Mi ONG')
        Subsidy.objects.create(presentation_date="2021-01-01", payment_date="2021-01-02", organism="ONG1",
                               provisional_resolution="2021-01-02", final_resolution="2021-01-03", amount=1000, name="Juan", ong=self.ong, status="Presentada")
        Subsidy.objects.create(presentation_date="2021-01-01", payment_date="2021-01-02", organism="ONG2",
                               provisional_resolution="2021-01-03", final_resolution="2021-01-04", amount=1000, name="Pedro", ong=self.ong, status="Presentada")
        Subsidy.objects.create(presentation_date="2021-01-01", payment_date="2021-01-02", organism="ONG3",
                               provisional_resolution="2021-01-07", final_resolution="2021-01-08", amount=1000, name="Maria", ong=self.ong, status="Presentada")

    def test_subsidy_create(self):
        subsidy = Subsidy.objects.get(name="Juan")
        self.assertEqual(subsidy.name, "Juan")
        self.assertEqual(subsidy.amount, 1000)
        self.assertEqual(str(subsidy.presentation_date), "2021-01-01")
        self.assertEqual(str(subsidy.payment_date), "2021-01-02")
        self.assertEqual(str(subsidy.provisional_resolution), "2021-01-02")
        self.assertEqual(str(subsidy.final_resolution), "2021-01-03")
        self.assertEqual(subsidy.organism, "ONG1")
        self.assertEqual(subsidy.ong.name, "Mi ONG")

    def test_subsidy_delete(self):
        subsidy = Subsidy.objects.get(name="Juan")
        subsidy.delete()
        self.assertEqual(Subsidy.objects.count(), 2)

    def test_subsidy_update(self):
        subsidy = Subsidy.objects.get(name="Juan")
        subsidy.name = "Juanito"
        subsidy.amount = 17
        subsidy.presentation_date = "2017-07-17"
        subsidy.payment_date = "2017-07-18"
        subsidy.provisional_resolution = "2017-07-18"
        subsidy.final_resolution = "2017-07-19"
        subsidy.organism = "ONG4"
        subsidy.save()
        self.assertEqual(subsidy.name, "Juanito")
        self.assertEqual(subsidy.amount, 17)
        self.assertEqual(str(subsidy.presentation_date), "2017-07-17")
        self.assertEqual(str(subsidy.payment_date), "2017-07-18")
        self.assertEqual(str(subsidy.provisional_resolution), "2017-07-18")
        self.assertEqual(str(subsidy.final_resolution), "2017-07-19")
        self.assertEqual(subsidy.organism, "ONG4")

    # Create test
    def test_subsidy_create_presentation_date_incorrect(self):
        with self.assertRaises(Exception):
            Subsidy.objects.create(presentation_date="This is a date incorrect", payment_date="2021-01-02", organism="ONG2",
                                   provisional_resolution="2017-07-18", final_resolution="2017-07-19", amount=1000, name="Pedro", ong=self.ong)

    def test_subsidy_create_presentation_justification_date_incorrect(self):
        with self.assertRaises(Exception):
            Subsidy.objects.create(presentation_date="2021-01-01",presentation_justification_date="This is a date incorrect", payment_date="2021-01-02", organism="ONG2",
                                   provisional_resolution="2017-07-18", final_resolution="2017-07-19", amount=1000, name="Pedro", ong=self.ong)

    def test_subsidy_create_payment_date_incorrect(self):
        with self.assertRaises(Exception):
            Subsidy.objects.create(presentation_date="2021-01-01", payment_date="This is a date incorrect", organism="ONG2",
                                   provisional_resolution="2017-07-18", final_resolution="2017-07-19", amount=1000, name="Pedro", ong=self.ong)

    def test_create_subsidy_organism_max_length_incorrect(self):
        with self.assertRaises(Exception):
            Subsidy.objects.create(presentation_date="2021-01-01", payment_date="2021-01-02", organism="ONG2"*100,
                                   provisional_resolution="2017-07-18", final_resolution="2017-07-19", amount=1000, name="Pedro", ong=self.ong)

    def test_subsidy_create_amount_negative(self):
        with self.assertRaises(Exception):
            Subsidy.objects.create(presentation_date="2021-01-01", payment_date="2021-01-02", organism="ONG2",
                                   provisional_resolution="2017-07-18", final_resolution="2017-07-19", amount=-1000, name="Pedro", ong=self.ong)

    def test_subsidy_create_name_max_length_incorrect(self):
        with self.assertRaises(Exception):
            Subsidy.objects.create(presentation_date="2021-01-01", payment_date="2021-01-02", organism="ONG1",
                                   provisional_resolution="2017-07-18", final_resolution="2017-07-19", amount=1000, name="Juan"*1000, ong=self.ong)

    def test_subsidy_create_name_null(self):
        with self.assertRaises(Exception):
            Subsidy.objects.create(presentation_date="2021-01-01", payment_date="2021-01-02", organism="ONG1",
                                   provisional_resolution="2017-07-18", final_resolution="2017-07-19", amount=1000, name=None, ong=self.ong)

    def test_subsidy_create_amount_null(self):
        with self.assertRaises(Exception):
            Subsidy.objects.create(presentation_date="2021-01-01", payment_date="2021-01-02", organism="ONG1",
                                   provisional_resolution="2017-07-18", final_resolution="2017-07-19", amount=None, name="Juan", ong=self.ong)

    def test_subsidy_create_organism_null(self):
        with self.assertRaises(Exception):
            Subsidy.objects.create(presentation_date="2021-01-01", payment_date="2021-01-02", organism=None,
                                   provisional_resolution="2017-07-18", final_resolution="2017-07-19", amount=1000, name="Juan", ong=self.ong)

    def test_subsidy_create_final_resolution_before_provisional(self):
        with self.assertRaises(Exception):
            Subsidy.objects.create(presentation_date="2021-01-01", payment_date="2021-01-02", organism="ONG2",provisional_resolution="2017-07-19", final_resolution="2017-07-18", amount=1000, name="Pedro",ong=self.ong)

    def test_subsidy_create_status_max_length_incorrect(self):
        with self.assertRaises(Exception):
            Subsidy.objects.create(presentation_date="2021-01-01", payment_date="2021-01-02", organism="ONG1",
                                   provisional_resolution="2017-07-18", final_resolution="2017-07-19", amount=1000, name="Juan"*1000, ong=self.ong, status="P"*51)

    def test_subsidy_create_status_null(self):
        with self.assertRaises(Exception):
            Subsidy.objects.create(presentation_date="2021-01-01", payment_date="2021-01-02", organism="ONG1",
                                   provisional_resolution="2017-07-18", final_resolution="2017-07-19", amount=1000, name="Juan"*1000, ong=self.ong, status=None)

    def test_subsidy_create_status_blank(self):
        with self.assertRaises(Exception):
            Subsidy.objects.create(presentation_date="2021-01-01", payment_date="2021-01-02", organism="ONG1",
                                   provisional_resolution="2017-07-18", final_resolution="2017-07-19", amount=1000, name="Juan"*1000, ong=self.ong, status="")

# TESTS UPDATE SUBSIDY

    def test_incorrect_amount_null(self):
            with self.assertRaises(Exception):
                self.subsidy.amount = None
                self.subsidy.save()

    def test_incorrect_amount_negative(self):
            with self.assertRaises(Exception):
                self.subsidy.amount = -1000
                self.subsidy.save()
    
    def test_incorrect_amount_string(self):
            with self.assertRaises(Exception):
                self.subsidy.amount = "Juan"
                self.subsidy.save()

    def test_incorrect_amount_bool(self):
            with self.assertRaises(Exception):
                self.subsidy.amount = True
                self.subsidy.save()
    
    def test_incorrect_payment_date_value_string_format(self):
            with self.assertRaises(Exception):
                self.subsidy.payment_date = "2010-23-12"
                self.subsidy.save()

    def test_incorrect_payment_date_value_string_format2(self):
            with self.assertRaises(Exception):
                self.subsidy.payment_date = "23/12/23"
                self.subsidy.save()

    def test_incorrect_payment_date_value_string_format3(self):
            with self.assertRaises(Exception):
                self.subsidy.payment_date = "23-12-23"
                self.subsidy.save()
    
    def test_incorrect_organism_null(self):
            with self.assertRaises(Exception):
                self.subsidy.organism = None
                self.subsidy.save()

    def test_incorrect_organism_max_length(self):
            with self.assertRaises(Exception):
                self.subsidy.organism = "ONG2"*100
                self.subsidy.save()

    def test_incorrect_name_null(self):
            with self.assertRaises(Exception):
                self.subsidy.name = None
                self.subsidy.save()

    def test_incorrect_name_max_length(self):
            with self.assertRaises(Exception):
                self.subsidy.name = "Juan"*1000
                self.subsidy.save()

    def test_incorrect_final_resolution_before_provisional(self):
            with self.assertRaises(Exception):
                self.subsidy.provisional_resolution = "2017-07-17"
                self.subsidy.final_resolution = "2017-07-18"
                self.subsidy.save()

    def test_incorrect_presentation_justification_date_before_presentation_date(self):
        with self.assertRaises(Exception):
            self.subsidy.presentation_justification_date = "2017-07-17"
            self.subsidy.presentation_date = "2017-07-18"
            self.subsidy.save()

    def test_incorrect_ong_null(self):
            with self.assertRaises(Exception):
                self.subsidy.ong = None
                self.subsidy.save()
    
    def test_incorrect_ong_value(self):
            with self.assertRaises(Exception):
                self.subsidy.ong = "ONG1"
                self.subsidy.save()

           


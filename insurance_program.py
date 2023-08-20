from typing import Any
from datetime import datetime
import persistent


class Program(persistent.Persistent):

    def __init__(self, code, insured, currency, lob, start_date, end_date):
        self.code = code
        self.insured = insured
        self.currency = currency
        self.line_of_business = lob
        self.start_date = start_date
        self.end_date = end_date
        self.creation_date = datetime.now
        self.last_modified = datetime.now

    def __repr__(self) -> str:
        return f"{self.code} {self.insured}"

    def __str__(self) -> str:
        return self.__repr__()
    
    def get_base_fields(self) -> list[tuple[str, str, Any]]:
        return [
            ("Insured", self.insured.get_absolute_url(), self.insured),
            ("Start date", "", self.start_date),
            ("End date", "", self.end_date),
            ("Currency", "", self.currency),
            ("Nr of layers", "", self.layer_set.all().count()),
        ]

    def get_fields_for_detail(self) -> list[tuple[str, str, Any]]: 
        fields = self.get_base_fields()
        fields.insert(0, ("Code", "", self.code))
        # layers = [
        #     (
        #         "",
        #         layer.get_absolute_url(),
        #         f"{layer}",
        #     )
        #     for layer in self.layer_set.all()
        # ]
        # fields.extend(layers)
        return fields

    def get_fields_for_list(self) -> list[tuple[str, str, Any]]:
        fields = self.get_base_fields()
        fields.insert(0, ("Code", self.get_absolute_url(), self.code))
        return fields
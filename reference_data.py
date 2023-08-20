from typing import Any
from abc import ABC, abstractmethod
import persistent

# class Reference_class(ABC):
#     @abstractmethod
#     def get_base_fields(self) -> list[tuple[str, str, Any]]:
#         pass

#     @abstractmethod
#     def get_fields_for_list(self) -> list[tuple[str, str, Any]]:
#         pass

#     @abstractmethod
#     def get_fields_for_detail(self) -> list[tuple[str, str, Any]]:
#         pass
    
####################

class Currency(persistent.Persistent):

    def __init__(self, name, iso_code_3):
        super().__init__()
        self.name = name
        self.iso_code_3 = iso_code_3

    def __repr__(self) -> str:
        return self.iso_code_3

    def __str__(self) -> str:
        return self.__repr__()
    
    def get_base_fields(self) -> list[tuple[str, str, Any]]:
        return [
            ("Name", "", self.name),
            ("Iso code", "", self.iso_code_3),
        ]
    
    def get_fields_for_detail(self) -> list[tuple[str, str, Any]]:
        return self.get_base_fields()

    def get_fields_for_list(self) -> list[tuple[str, str, Any]]:
        fields = self.get_base_fields()
        return fields
    
#####################

class Country(persistent.Persistent):

    def __init__(self, name, iso_code_3):
        self.name = name
        self.iso_code_3 = iso_code_3

    def __repr__(self) -> str:
        return self.iso_code_3

    def __str__(self) -> str:
        return self.__repr__()
    
    def get_base_fields(self) -> list[tuple[str, str, Any]]:
        return [
            ("Name", "", self.name),
            ("Iso code", "", self.iso_code_3),
        ]
    
    def get_fields_for_list(self) -> list[tuple[str, str, Any]]:
        fields = self.get_base_fields()
        return fields
    
#######################

class Company(persistent.Persistent):

    def __init__(self, name, country, email):
        self.name = name
        self.country = country
        self.email = email

    @staticmethod
    def type_string():
        return "Company"

    def __repr__(self) -> str:
        return f"{self.name}"

    def __str__(self) -> str:
        return self.__repr__()

    def get_base_fields(self) -> list[tuple[str, str, Any]]:
        return [
            ("Country", "", self.country.name),
            ("E-mail", "", self.email),
        ]

    def get_fields_for_detail(self) -> list[tuple[str, str, Any]]:
        fields = self.get_base_fields()
        fields.insert(0, ("Name", "", self.name))
        return fields

    def get_fields_for_list(self) -> list[tuple[str, str, Any]]:
        fields = self.get_base_fields()
        fields.insert(0, ("Name", self.get_absolute_url(), self.name))
        return fields
    
###################


class Classification(persistent.Persistent):
    # PROPERTY = "Property"
    # CASULATY = "Casualty"
    # AGRICULTURE = "Agriculture"
    # MOTOR = "Motor"
    # LOB_TYPES = (
    #     (PROPERTY, "Property"),
    #     (CASULATY, "Casualty"),
    #     (AGRICULTURE, "Agriculture"),
    #     (MOTOR, "Motor"),
    # )

    def __init__(self, name):
        self.name = name

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.__repr__()

    def get_base_fields(self) -> list[tuple[str, str, Any]]:
        return [
            ("Name", "", self.name),
        ]
    
    def get_fields_for_list(self) -> list[tuple[str, str, Any]]:
        fields = self.get_base_fields()
        return fields
    

########


class CodeGenerator(persistent.Persistent):
    
    def __init__(self):
        self.codes = []

    def create_next_code(self, prefix):
        q = [code for code in self.codes if code[0] == prefix]
        if len(q) == 0:
            nc = 1
        else:
            q.sort(reverse=True)
            nc = int(q[-1][1:]) + 1
            code = f'{prefix}{str(nc).zfill(5)}'
            self.codes.append(code)
            return code
    
    def next_program_code(self):
        prefix = "P"
        return self.create_next_code(prefix)
    
    def next_layer_code(self):
        prefix = "L"
        return self.create_next_code(prefix)
    
    def next_contract_code(self):
        prefix = "C"
        return self.create_next_code(prefix)

    def next_analysis_code(self):
        prefix = "A"
        return self.create_next_code(prefix)
    
    def next_risk_profile_code(self):
        prefix = "R"
        return self.create_next_code(prefix)
    
    def next_loss_profile_code(self):
        prefix = "S"
        return self.create_next_code(prefix)
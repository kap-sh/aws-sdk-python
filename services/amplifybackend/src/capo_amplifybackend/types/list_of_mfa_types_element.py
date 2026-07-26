"""Generated from Smithy shape ``com.amazonaws.amplifybackend#ListOfMfaTypesElement``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_amplifybackend.types.mfa_types_element

ListOfMfaTypesElement: TypeAlias = list[
    "capo_amplifybackend.types.mfa_types_element.MfaTypesElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfMfaTypesElement) -> list:
    import capo_amplifybackend.types.mfa_types_element

    out: list = []
    for item in value:
        out.append(capo_amplifybackend.types.mfa_types_element.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfMfaTypesElement:
    import capo_amplifybackend.types.mfa_types_element

    out: ListOfMfaTypesElement = []
    for item in data:
        out.append(capo_amplifybackend.types.mfa_types_element.deserialize_json(item))
    return out

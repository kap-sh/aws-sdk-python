"""Generated from Smithy shape ``com.amazonaws.customerprofiles#StandardIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.standard_identifier

StandardIdentifierList: TypeAlias = list[
    "capo_customer_profiles.types.standard_identifier.StandardIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: StandardIdentifierList) -> list:
    import capo_customer_profiles.types.standard_identifier

    out: list = []
    for item in value:
        out.append(
            capo_customer_profiles.types.standard_identifier.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> StandardIdentifierList:
    import capo_customer_profiles.types.standard_identifier

    out: StandardIdentifierList = []
    for item in data:
        out.append(
            capo_customer_profiles.types.standard_identifier.deserialize_json(item)
        )
    return out

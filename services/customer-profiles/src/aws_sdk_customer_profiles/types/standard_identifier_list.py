"""Generated from Smithy shape ``com.amazonaws.customerprofiles#StandardIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.standard_identifier

StandardIdentifierList: TypeAlias = list[
    "aws_sdk_customer_profiles.types.standard_identifier.StandardIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: StandardIdentifierList) -> list:
    import aws_sdk_customer_profiles.types.standard_identifier

    out: list = []
    for item in value:
        out.append(
            aws_sdk_customer_profiles.types.standard_identifier.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> StandardIdentifierList:
    import aws_sdk_customer_profiles.types.standard_identifier

    out: StandardIdentifierList = []
    for item in data:
        out.append(
            aws_sdk_customer_profiles.types.standard_identifier.deserialize_json(item)
        )
    return out

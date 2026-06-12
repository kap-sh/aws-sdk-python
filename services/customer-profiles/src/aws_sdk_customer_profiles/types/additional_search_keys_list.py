"""Generated from Smithy shape ``com.amazonaws.customerprofiles#additionalSearchKeysList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.additional_search_key

additionalSearchKeysList: TypeAlias = list[
    "aws_sdk_customer_profiles.types.additional_search_key.AdditionalSearchKey"
]


# --- restJson1 ser/de ---
def serialize_json(value: additionalSearchKeysList) -> list:
    import aws_sdk_customer_profiles.types.additional_search_key

    out: list = []
    for item in value:
        out.append(
            aws_sdk_customer_profiles.types.additional_search_key.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> additionalSearchKeysList:
    import aws_sdk_customer_profiles.types.additional_search_key

    out: additionalSearchKeysList = []
    for item in data:
        out.append(
            aws_sdk_customer_profiles.types.additional_search_key.deserialize_json(item)
        )
    return out

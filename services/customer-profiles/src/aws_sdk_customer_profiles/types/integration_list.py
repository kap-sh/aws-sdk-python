"""Generated from Smithy shape ``com.amazonaws.customerprofiles#IntegrationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.list_integration_item

IntegrationList: TypeAlias = list[
    "aws_sdk_customer_profiles.types.list_integration_item.ListIntegrationItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: IntegrationList) -> list:
    import aws_sdk_customer_profiles.types.list_integration_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_customer_profiles.types.list_integration_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> IntegrationList:
    import aws_sdk_customer_profiles.types.list_integration_item

    out: IntegrationList = []
    for item in data:
        out.append(
            aws_sdk_customer_profiles.types.list_integration_item.deserialize_json(item)
        )
    return out

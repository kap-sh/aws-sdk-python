"""Generated from Smithy shape ``com.amazonaws.customerprofiles#IntegrationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.list_integration_item

IntegrationList: TypeAlias = list[
    "capo_customer_profiles.types.list_integration_item.ListIntegrationItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: IntegrationList) -> list:
    import capo_customer_profiles.types.list_integration_item

    out: list = []
    for item in value:
        out.append(
            capo_customer_profiles.types.list_integration_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> IntegrationList:
    import capo_customer_profiles.types.list_integration_item

    out: IntegrationList = []
    for item in data:
        out.append(
            capo_customer_profiles.types.list_integration_item.deserialize_json(item)
        )
    return out

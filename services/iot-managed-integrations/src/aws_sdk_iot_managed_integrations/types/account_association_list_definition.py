"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#AccountAssociationListDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.account_association_item

AccountAssociationListDefinition: TypeAlias = list[
    "aws_sdk_iot_managed_integrations.types.account_association_item.AccountAssociationItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccountAssociationListDefinition) -> list:
    import aws_sdk_iot_managed_integrations.types.account_association_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_managed_integrations.types.account_association_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AccountAssociationListDefinition:
    import aws_sdk_iot_managed_integrations.types.account_association_item

    out: AccountAssociationListDefinition = []
    for item in data:
        out.append(
            aws_sdk_iot_managed_integrations.types.account_association_item.deserialize_json(
                item
            )
        )
    return out

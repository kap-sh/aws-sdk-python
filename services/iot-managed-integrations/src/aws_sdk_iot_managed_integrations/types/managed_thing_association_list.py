"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ManagedThingAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.managed_thing_association

ManagedThingAssociationList: TypeAlias = list[
    "aws_sdk_iot_managed_integrations.types.managed_thing_association.ManagedThingAssociation"
]


# --- restJson1 ser/de ---
def serialize_json(value: ManagedThingAssociationList) -> list:
    import aws_sdk_iot_managed_integrations.types.managed_thing_association

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_managed_integrations.types.managed_thing_association.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ManagedThingAssociationList:
    import aws_sdk_iot_managed_integrations.types.managed_thing_association

    out: ManagedThingAssociationList = []
    for item in data:
        out.append(
            aws_sdk_iot_managed_integrations.types.managed_thing_association.deserialize_json(
                item
            )
        )
    return out

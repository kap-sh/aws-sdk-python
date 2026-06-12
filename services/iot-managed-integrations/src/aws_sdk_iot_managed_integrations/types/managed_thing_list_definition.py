"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ManagedThingListDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.managed_thing_summary

ManagedThingListDefinition: TypeAlias = list[
    "aws_sdk_iot_managed_integrations.types.managed_thing_summary.ManagedThingSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ManagedThingListDefinition) -> list:
    import aws_sdk_iot_managed_integrations.types.managed_thing_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_managed_integrations.types.managed_thing_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ManagedThingListDefinition:
    import aws_sdk_iot_managed_integrations.types.managed_thing_summary

    out: ManagedThingListDefinition = []
    for item in data:
        out.append(
            aws_sdk_iot_managed_integrations.types.managed_thing_summary.deserialize_json(
                item
            )
        )
    return out

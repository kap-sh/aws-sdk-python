"""Generated from Smithy shape ``com.amazonaws.greengrassv2#AssociatedClientDeviceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.associated_client_device

AssociatedClientDeviceList: TypeAlias = list[
    "aws_sdk_greengrassv2.types.associated_client_device.AssociatedClientDevice"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedClientDeviceList) -> list:
    import aws_sdk_greengrassv2.types.associated_client_device

    out: list = []
    for item in value:
        out.append(
            aws_sdk_greengrassv2.types.associated_client_device.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AssociatedClientDeviceList:
    import aws_sdk_greengrassv2.types.associated_client_device

    out: AssociatedClientDeviceList = []
    for item in data:
        out.append(
            aws_sdk_greengrassv2.types.associated_client_device.deserialize_json(item)
        )
    return out

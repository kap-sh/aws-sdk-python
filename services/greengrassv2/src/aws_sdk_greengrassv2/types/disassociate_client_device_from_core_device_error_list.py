"""Generated from Smithy shape ``com.amazonaws.greengrassv2#DisassociateClientDeviceFromCoreDeviceErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.disassociate_client_device_from_core_device_error_entry

DisassociateClientDeviceFromCoreDeviceErrorList: TypeAlias = list[
    "aws_sdk_greengrassv2.types.disassociate_client_device_from_core_device_error_entry.DisassociateClientDeviceFromCoreDeviceErrorEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateClientDeviceFromCoreDeviceErrorList) -> list:
    import aws_sdk_greengrassv2.types.disassociate_client_device_from_core_device_error_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_greengrassv2.types.disassociate_client_device_from_core_device_error_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DisassociateClientDeviceFromCoreDeviceErrorList:
    import aws_sdk_greengrassv2.types.disassociate_client_device_from_core_device_error_entry

    out: DisassociateClientDeviceFromCoreDeviceErrorList = []
    for item in data:
        out.append(
            aws_sdk_greengrassv2.types.disassociate_client_device_from_core_device_error_entry.deserialize_json(
                item
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.greengrassv2#DisassociateClientDeviceFromCoreDeviceEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_greengrassv2.types.disassociate_client_device_from_core_device_entry

DisassociateClientDeviceFromCoreDeviceEntryList: TypeAlias = list[
    "capo_greengrassv2.types.disassociate_client_device_from_core_device_entry.DisassociateClientDeviceFromCoreDeviceEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateClientDeviceFromCoreDeviceEntryList) -> list:
    import capo_greengrassv2.types.disassociate_client_device_from_core_device_entry

    out: list = []
    for item in value:
        out.append(
            capo_greengrassv2.types.disassociate_client_device_from_core_device_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DisassociateClientDeviceFromCoreDeviceEntryList:
    import capo_greengrassv2.types.disassociate_client_device_from_core_device_entry

    out: DisassociateClientDeviceFromCoreDeviceEntryList = []
    for item in data:
        out.append(
            capo_greengrassv2.types.disassociate_client_device_from_core_device_entry.deserialize_json(
                item
            )
        )
    return out

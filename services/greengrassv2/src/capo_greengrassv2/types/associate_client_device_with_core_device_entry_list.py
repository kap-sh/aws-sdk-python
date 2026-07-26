"""Generated from Smithy shape ``com.amazonaws.greengrassv2#AssociateClientDeviceWithCoreDeviceEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_greengrassv2.types.associate_client_device_with_core_device_entry

AssociateClientDeviceWithCoreDeviceEntryList: TypeAlias = list[
    "capo_greengrassv2.types.associate_client_device_with_core_device_entry.AssociateClientDeviceWithCoreDeviceEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociateClientDeviceWithCoreDeviceEntryList) -> list:
    import capo_greengrassv2.types.associate_client_device_with_core_device_entry

    out: list = []
    for item in value:
        out.append(
            capo_greengrassv2.types.associate_client_device_with_core_device_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssociateClientDeviceWithCoreDeviceEntryList:
    import capo_greengrassv2.types.associate_client_device_with_core_device_entry

    out: AssociateClientDeviceWithCoreDeviceEntryList = []
    for item in data:
        out.append(
            capo_greengrassv2.types.associate_client_device_with_core_device_entry.deserialize_json(
                item
            )
        )
    return out

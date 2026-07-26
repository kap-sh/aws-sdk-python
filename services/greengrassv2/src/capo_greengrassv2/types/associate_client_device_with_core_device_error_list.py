"""Generated from Smithy shape ``com.amazonaws.greengrassv2#AssociateClientDeviceWithCoreDeviceErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_greengrassv2.types.associate_client_device_with_core_device_error_entry

AssociateClientDeviceWithCoreDeviceErrorList: TypeAlias = list[
    "capo_greengrassv2.types.associate_client_device_with_core_device_error_entry.AssociateClientDeviceWithCoreDeviceErrorEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociateClientDeviceWithCoreDeviceErrorList) -> list:
    import capo_greengrassv2.types.associate_client_device_with_core_device_error_entry

    out: list = []
    for item in value:
        out.append(
            capo_greengrassv2.types.associate_client_device_with_core_device_error_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssociateClientDeviceWithCoreDeviceErrorList:
    import capo_greengrassv2.types.associate_client_device_with_core_device_error_entry

    out: AssociateClientDeviceWithCoreDeviceErrorList = []
    for item in data:
        out.append(
            capo_greengrassv2.types.associate_client_device_with_core_device_error_entry.deserialize_json(
                item
            )
        )
    return out

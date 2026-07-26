"""Generated from Smithy shape ``com.amazonaws.greengrassv2#BatchAssociateClientDeviceWithCoreDeviceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.associate_client_device_with_core_device_entry_list
    import capo_greengrassv2.types.io_t_thing_name


class BatchAssociateClientDeviceWithCoreDeviceRequest(TypedDict, closed=True):
    entries: NotRequired[
        "capo_greengrassv2.types.associate_client_device_with_core_device_entry_list.AssociateClientDeviceWithCoreDeviceEntryList"
    ]
    """<p>The list of client devices to associate.</p>"""
    core_device_thing_name: "capo_greengrassv2.types.io_t_thing_name.IoTThingName"
    """<p>The name of the core device. This is also the name of the IoT thing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchAssociateClientDeviceWithCoreDeviceRequest) -> dict:
    out: dict = {}
    if "entries" in value:
        import capo_greengrassv2.types.associate_client_device_with_core_device_entry_list

        out["entries"] = (
            capo_greengrassv2.types.associate_client_device_with_core_device_entry_list.serialize_json(
                value["entries"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchAssociateClientDeviceWithCoreDeviceRequest:
    out: BatchAssociateClientDeviceWithCoreDeviceRequest = {}  # type: ignore[typeddict-item]
    if "entries" in data:
        import capo_greengrassv2.types.associate_client_device_with_core_device_entry_list

        out["entries"] = (
            capo_greengrassv2.types.associate_client_device_with_core_device_entry_list.deserialize_json(
                data["entries"]
            )
        )
    return out

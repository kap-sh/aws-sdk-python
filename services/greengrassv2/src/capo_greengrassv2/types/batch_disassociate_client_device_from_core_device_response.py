"""Generated from Smithy shape ``com.amazonaws.greengrassv2#BatchDisassociateClientDeviceFromCoreDeviceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.disassociate_client_device_from_core_device_error_list


class BatchDisassociateClientDeviceFromCoreDeviceResponse(TypedDict, closed=True):
    error_entries: NotRequired[
        "capo_greengrassv2.types.disassociate_client_device_from_core_device_error_list.DisassociateClientDeviceFromCoreDeviceErrorList"
    ]
    """<p>The list of any errors for the entries in the request. Each error entry contains the name of the IoT thing that failed to disassociate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDisassociateClientDeviceFromCoreDeviceResponse) -> dict:
    out: dict = {}
    if "error_entries" in value:
        import capo_greengrassv2.types.disassociate_client_device_from_core_device_error_list

        out["errorEntries"] = (
            capo_greengrassv2.types.disassociate_client_device_from_core_device_error_list.serialize_json(
                value["error_entries"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchDisassociateClientDeviceFromCoreDeviceResponse:
    out: BatchDisassociateClientDeviceFromCoreDeviceResponse = {}  # type: ignore[typeddict-item]
    if "errorEntries" in data:
        import capo_greengrassv2.types.disassociate_client_device_from_core_device_error_list

        out["error_entries"] = (
            capo_greengrassv2.types.disassociate_client_device_from_core_device_error_list.deserialize_json(
                data["errorEntries"]
            )
        )
    return out

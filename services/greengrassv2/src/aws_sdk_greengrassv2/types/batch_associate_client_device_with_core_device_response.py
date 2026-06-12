"""Generated from Smithy shape ``com.amazonaws.greengrassv2#BatchAssociateClientDeviceWithCoreDeviceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.associate_client_device_with_core_device_error_list


class BatchAssociateClientDeviceWithCoreDeviceResponse(TypedDict):
    error_entries: NotRequired[
        "aws_sdk_greengrassv2.types.associate_client_device_with_core_device_error_list.AssociateClientDeviceWithCoreDeviceErrorList"
    ]
    """<p>The list of any errors for the entries in the request. Each error entry contains the name of the IoT thing that failed to associate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchAssociateClientDeviceWithCoreDeviceResponse) -> dict:
    out: dict = {}
    if "error_entries" in value:
        import aws_sdk_greengrassv2.types.associate_client_device_with_core_device_error_list

        out["errorEntries"] = (
            aws_sdk_greengrassv2.types.associate_client_device_with_core_device_error_list.serialize_json(
                value["error_entries"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchAssociateClientDeviceWithCoreDeviceResponse:
    out: BatchAssociateClientDeviceWithCoreDeviceResponse = {}  # type: ignore[typeddict-item]
    if "errorEntries" in data:
        import aws_sdk_greengrassv2.types.associate_client_device_with_core_device_error_list

        out["error_entries"] = (
            aws_sdk_greengrassv2.types.associate_client_device_with_core_device_error_list.deserialize_json(
                data["errorEntries"]
            )
        )
    return out

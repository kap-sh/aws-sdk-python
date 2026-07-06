"""Generated from Smithy shape ``com.amazonaws.medialive#ListInputDevicesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_input_device_summary
    import aws_sdk_medialive.types.__string


class ListInputDevicesResponse(TypedDict, closed=True):
    input_devices: NotRequired[
        "aws_sdk_medialive.types.__list_of_input_device_summary.__listOfInputDeviceSummary"
    ]
    """The list of input devices."""
    next_token: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """A token to get additional list results."""


# --- restJson1 ser/de ---
def serialize_json(value: ListInputDevicesResponse) -> dict:
    out: dict = {}
    if "input_devices" in value:
        import aws_sdk_medialive.types.__list_of_input_device_summary

        out["inputDevices"] = (
            aws_sdk_medialive.types.__list_of_input_device_summary.serialize_json(
                value["input_devices"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInputDevicesResponse:
    out: ListInputDevicesResponse = {}  # type: ignore[typeddict-item]
    if "inputDevices" in data:
        import aws_sdk_medialive.types.__list_of_input_device_summary

        out["input_devices"] = (
            aws_sdk_medialive.types.__list_of_input_device_summary.deserialize_json(
                data["inputDevices"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out

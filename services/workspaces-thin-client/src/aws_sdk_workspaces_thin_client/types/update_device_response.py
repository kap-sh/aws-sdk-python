"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#UpdateDeviceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces_thin_client.types.device_summary


class UpdateDeviceResponse(TypedDict):
    device: NotRequired[
        "aws_sdk_workspaces_thin_client.types.device_summary.DeviceSummary"
    ]
    """<p>Describes a device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDeviceResponse) -> dict:
    out: dict = {}
    if "device" in value:
        import aws_sdk_workspaces_thin_client.types.device_summary

        out["device"] = (
            aws_sdk_workspaces_thin_client.types.device_summary.serialize_json(
                value["device"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateDeviceResponse:
    out: UpdateDeviceResponse = {}  # type: ignore[typeddict-item]
    if "device" in data:
        import aws_sdk_workspaces_thin_client.types.device_summary

        out["device"] = (
            aws_sdk_workspaces_thin_client.types.device_summary.deserialize_json(
                data["device"]
            )
        )
    return out

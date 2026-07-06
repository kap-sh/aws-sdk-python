"""Generated from Smithy shape ``com.amazonaws.braket#SearchDevicesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_braket.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_braket.types.device_summary_list


class SearchDevicesResponse(TypedDict, closed=True):
    devices: "aws_sdk_braket.types.device_summary_list.DeviceSummaryList"
    """<p>An array of <code>DeviceSummary</code> objects for devices that match the specified filter values.</p>"""
    next_token: NotRequired["str"]
    """<p>A token used for pagination of results, or null if there are no additional results. Use the token value in a subsequent request to continue search where the previous request ended.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchDevicesResponse) -> dict:
    out: dict = {}
    import aws_sdk_braket.types.device_summary_list

    out["devices"] = aws_sdk_braket.types.device_summary_list.serialize_json(
        value["devices"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchDevicesResponse:
    out: SearchDevicesResponse = {}  # type: ignore[typeddict-item]
    if "devices" in data:
        import aws_sdk_braket.types.device_summary_list

        out["devices"] = aws_sdk_braket.types.device_summary_list.deserialize_json(
            data["devices"]
        )
    else:
        raise DeserializationError("SearchDevicesResponse.devices required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out

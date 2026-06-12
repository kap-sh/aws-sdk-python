"""Generated from Smithy shape ``com.amazonaws.swf#RecordMarkerDecisionAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.data
    import aws_sdk_swf.types.marker_name


class RecordMarkerDecisionAttributes(TypedDict):
    marker_name: "aws_sdk_swf.types.marker_name.MarkerName"
    """<p> The name of the marker.</p>"""
    details: NotRequired["aws_sdk_swf.types.data.Data"]
    """<p> The details of the marker.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecordMarkerDecisionAttributes) -> dict:
    out: dict = {}
    out["markerName"] = value["marker_name"]
    if "details" in value:
        out["details"] = value["details"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RecordMarkerDecisionAttributes:
    out: RecordMarkerDecisionAttributes = {}  # type: ignore[typeddict-item]
    if "markerName" in data:
        out["marker_name"] = data["markerName"]
    else:
        raise DeserializationError(
            "RecordMarkerDecisionAttributes.marker_name required"
        )
    if "details" in data:
        out["details"] = data["details"]
    return out

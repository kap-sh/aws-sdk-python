"""Generated from Smithy shape ``com.amazonaws.frauddetector#EventVariableSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.sensitive_string


class EventVariableSummary(TypedDict):
    name: NotRequired["aws_sdk_frauddetector.types.sensitive_string.sensitiveString"]
    """<p> The event variable name. </p>"""
    value: NotRequired["aws_sdk_frauddetector.types.sensitive_string.sensitiveString"]
    """<p> The value of the event variable. </p>"""
    source: NotRequired["aws_sdk_frauddetector.types.sensitive_string.sensitiveString"]
    """<p> The event variable source. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventVariableSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "value" in value:
        out["value"] = value["value"]
    if "source" in value:
        out["source"] = value["source"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EventVariableSummary:
    out: EventVariableSummary = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "value" in data:
        out["value"] = data["value"]
    if "source" in data:
        out["source"] = data["source"]
    return out

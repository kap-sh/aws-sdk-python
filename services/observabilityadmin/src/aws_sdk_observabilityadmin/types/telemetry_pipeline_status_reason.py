"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TelemetryPipelineStatusReason``."""

from typing_extensions import NotRequired, TypedDict


class TelemetryPipelineStatusReason(TypedDict, closed=True):
    description: NotRequired["str"]
    """<p>A description of the pipeline status reason, providing additional context about the current state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TelemetryPipelineStatusReason) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> TelemetryPipelineStatusReason:
    out: TelemetryPipelineStatusReason = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    return out

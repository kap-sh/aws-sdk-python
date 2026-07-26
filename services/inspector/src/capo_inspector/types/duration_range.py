"""Generated from Smithy shape ``com.amazonaws.inspector#DurationRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.assessment_run_duration


class DurationRange(TypedDict, closed=True):
    min_seconds: NotRequired[
        "capo_inspector.types.assessment_run_duration.AssessmentRunDuration"
    ]
    """<p>The minimum value of the duration range. Must be greater than zero.</p>"""
    max_seconds: NotRequired[
        "capo_inspector.types.assessment_run_duration.AssessmentRunDuration"
    ]
    """<p>The maximum value of the duration range. Must be less than or equal to 604800 seconds (1 week).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DurationRange) -> dict:
    out: dict = {}
    if "min_seconds" in value:
        out["minSeconds"] = value["min_seconds"]
    if "max_seconds" in value:
        out["maxSeconds"] = value["max_seconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DurationRange:
    out: DurationRange = {}  # type: ignore[typeddict-item]
    if "minSeconds" in data:
        out["min_seconds"] = data["minSeconds"]
    if "maxSeconds" in data:
        out["max_seconds"] = data["maxSeconds"]
    return out

"""Generated from Smithy shape ``com.amazonaws.inspector#AssessmentTargetFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector.types.name_pattern


class AssessmentTargetFilter(TypedDict, closed=True):
    assessment_target_name_pattern: NotRequired[
        "aws_sdk_inspector.types.name_pattern.NamePattern"
    ]
    """<p>For a record to match a filter, an explicit value or a string that contains a wildcard that is specified for this data type property must match the value of the <b>assessmentTargetName</b> property of the <a>AssessmentTarget</a> data type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssessmentTargetFilter) -> dict:
    out: dict = {}
    if "assessment_target_name_pattern" in value:
        out["assessmentTargetNamePattern"] = value["assessment_target_name_pattern"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssessmentTargetFilter:
    out: AssessmentTargetFilter = {}  # type: ignore[typeddict-item]
    if "assessmentTargetNamePattern" in data:
        out["assessment_target_name_pattern"] = data["assessmentTargetNamePattern"]
    return out

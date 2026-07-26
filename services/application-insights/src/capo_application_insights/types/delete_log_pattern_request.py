"""Generated from Smithy shape ``com.amazonaws.applicationinsights#DeleteLogPatternRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_application_insights.errors import DeserializationError

if TYPE_CHECKING:
    import capo_application_insights.types.log_pattern_name
    import capo_application_insights.types.log_pattern_set_name
    import capo_application_insights.types.resource_group_name


class DeleteLogPatternRequest(TypedDict, closed=True):
    resource_group_name: (
        "capo_application_insights.types.resource_group_name.ResourceGroupName"
    )
    """<p>The name of the resource group.</p>"""
    pattern_set_name: (
        "capo_application_insights.types.log_pattern_set_name.LogPatternSetName"
    )
    """<p>The name of the log pattern set.</p>"""
    pattern_name: "capo_application_insights.types.log_pattern_name.LogPatternName"
    """<p>The name of the log pattern.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteLogPatternRequest) -> dict:
    out: dict = {}
    out["ResourceGroupName"] = value["resource_group_name"]
    out["PatternSetName"] = value["pattern_set_name"]
    out["PatternName"] = value["pattern_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteLogPatternRequest:
    out: DeleteLogPatternRequest = {}  # type: ignore[typeddict-item]
    if "ResourceGroupName" in data:
        out["resource_group_name"] = data["ResourceGroupName"]
    else:
        raise DeserializationError(
            "DeleteLogPatternRequest.resource_group_name required"
        )
    if "PatternSetName" in data:
        out["pattern_set_name"] = data["PatternSetName"]
    else:
        raise DeserializationError("DeleteLogPatternRequest.pattern_set_name required")
    if "PatternName" in data:
        out["pattern_name"] = data["PatternName"]
    else:
        raise DeserializationError("DeleteLogPatternRequest.pattern_name required")
    return out

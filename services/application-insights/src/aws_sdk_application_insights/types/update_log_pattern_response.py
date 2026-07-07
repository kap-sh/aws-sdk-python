"""Generated from Smithy shape ``com.amazonaws.applicationinsights#UpdateLogPatternResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.log_pattern
    import aws_sdk_application_insights.types.resource_group_name


class UpdateLogPatternResponse(TypedDict, closed=True):
    resource_group_name: NotRequired[
        "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName"
    ]
    """<p>The name of the resource group.</p>"""
    log_pattern: NotRequired[
        "aws_sdk_application_insights.types.log_pattern.LogPattern"
    ]
    """<p>The successfully created log pattern.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLogPatternResponse) -> dict:
    out: dict = {}
    if "resource_group_name" in value:
        out["ResourceGroupName"] = value["resource_group_name"]
    if "log_pattern" in value:
        import aws_sdk_application_insights.types.log_pattern

        out["LogPattern"] = (
            aws_sdk_application_insights.types.log_pattern.serialize_aws_json_1_1(
                value["log_pattern"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateLogPatternResponse:
    out: UpdateLogPatternResponse = {}  # type: ignore[typeddict-item]
    if "ResourceGroupName" in data:
        out["resource_group_name"] = data["ResourceGroupName"]
    if "LogPattern" in data:
        import aws_sdk_application_insights.types.log_pattern

        out["log_pattern"] = (
            aws_sdk_application_insights.types.log_pattern.deserialize_aws_json_1_1(
                data["LogPattern"]
            )
        )
    return out

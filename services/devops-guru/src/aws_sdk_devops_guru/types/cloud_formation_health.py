"""Generated from Smithy shape ``com.amazonaws.devopsguru#CloudFormationHealth``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.analyzed_resource_count
    import aws_sdk_devops_guru.types.insight_health
    import aws_sdk_devops_guru.types.stack_name


class CloudFormationHealth(TypedDict, closed=True):
    stack_name: NotRequired["aws_sdk_devops_guru.types.stack_name.StackName"]
    """<p> The name of the CloudFormation stack. </p>"""
    insight: NotRequired["aws_sdk_devops_guru.types.insight_health.InsightHealth"]
    """<p> Information about the health of the Amazon Web Services resources in your account that are specified by an Amazon Web Services CloudFormation stack, including the number of open proactive, open reactive insights, and the Mean Time to Recover (MTTR) of closed insights. </p>"""
    analyzed_resource_count: NotRequired[
        "aws_sdk_devops_guru.types.analyzed_resource_count.AnalyzedResourceCount"
    ]
    """<p> Number of resources that DevOps Guru is monitoring in your account that are specified by an Amazon Web Services CloudFormation stack. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudFormationHealth) -> dict:
    out: dict = {}
    if "stack_name" in value:
        out["StackName"] = value["stack_name"]
    if "insight" in value:
        import aws_sdk_devops_guru.types.insight_health

        out["Insight"] = aws_sdk_devops_guru.types.insight_health.serialize_json(
            value["insight"]
        )
    if "analyzed_resource_count" in value:
        out["AnalyzedResourceCount"] = value["analyzed_resource_count"]
    return out


def deserialize_json(data: dict) -> CloudFormationHealth:
    out: CloudFormationHealth = {}  # type: ignore[typeddict-item]
    if "StackName" in data:
        out["stack_name"] = data["StackName"]
    if "Insight" in data:
        import aws_sdk_devops_guru.types.insight_health

        out["insight"] = aws_sdk_devops_guru.types.insight_health.deserialize_json(
            data["Insight"]
        )
    if "AnalyzedResourceCount" in data:
        out["analyzed_resource_count"] = data["AnalyzedResourceCount"]
    return out

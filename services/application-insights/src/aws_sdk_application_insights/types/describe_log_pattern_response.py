"""Generated from Smithy shape ``com.amazonaws.applicationinsights#DescribeLogPatternResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.account_id
    import aws_sdk_application_insights.types.log_pattern
    import aws_sdk_application_insights.types.resource_group_name


class DescribeLogPatternResponse(TypedDict):
    resource_group_name: NotRequired[
        "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName"
    ]
    """<p>The name of the resource group.</p>"""
    account_id: NotRequired["aws_sdk_application_insights.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID for the resource group owner.</p>"""
    log_pattern: NotRequired[
        "aws_sdk_application_insights.types.log_pattern.LogPattern"
    ]
    """<p>The successfully created log pattern.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLogPatternResponse) -> dict:
    out: dict = {}
    if "resource_group_name" in value:
        out["ResourceGroupName"] = value["resource_group_name"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "log_pattern" in value:
        import aws_sdk_application_insights.types.log_pattern

        out["LogPattern"] = (
            aws_sdk_application_insights.types.log_pattern.serialize_aws_json_1_1(
                value["log_pattern"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLogPatternResponse:
    out: DescribeLogPatternResponse = {}  # type: ignore[typeddict-item]
    if "ResourceGroupName" in data:
        out["resource_group_name"] = data["ResourceGroupName"]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "LogPattern" in data:
        import aws_sdk_application_insights.types.log_pattern

        out["log_pattern"] = (
            aws_sdk_application_insights.types.log_pattern.deserialize_aws_json_1_1(
                data["LogPattern"]
            )
        )
    return out

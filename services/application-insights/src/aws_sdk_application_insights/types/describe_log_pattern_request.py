"""Generated from Smithy shape ``com.amazonaws.applicationinsights#DescribeLogPatternRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_application_insights.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.account_id
    import aws_sdk_application_insights.types.log_pattern_name
    import aws_sdk_application_insights.types.log_pattern_set_name
    import aws_sdk_application_insights.types.resource_group_name


class DescribeLogPatternRequest(TypedDict):
    resource_group_name: (
        "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName"
    )
    """<p>The name of the resource group.</p>"""
    pattern_set_name: (
        "aws_sdk_application_insights.types.log_pattern_set_name.LogPatternSetName"
    )
    """<p>The name of the log pattern set.</p>"""
    pattern_name: "aws_sdk_application_insights.types.log_pattern_name.LogPatternName"
    """<p>The name of the log pattern.</p>"""
    account_id: NotRequired["aws_sdk_application_insights.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID for the resource group owner.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLogPatternRequest) -> dict:
    out: dict = {}
    out["ResourceGroupName"] = value["resource_group_name"]
    out["PatternSetName"] = value["pattern_set_name"]
    out["PatternName"] = value["pattern_name"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLogPatternRequest:
    out: DescribeLogPatternRequest = {}  # type: ignore[typeddict-item]
    if "ResourceGroupName" in data:
        out["resource_group_name"] = data["ResourceGroupName"]
    else:
        raise DeserializationError(
            "DescribeLogPatternRequest.resource_group_name required"
        )
    if "PatternSetName" in data:
        out["pattern_set_name"] = data["PatternSetName"]
    else:
        raise DeserializationError(
            "DescribeLogPatternRequest.pattern_set_name required"
        )
    if "PatternName" in data:
        out["pattern_name"] = data["PatternName"]
    else:
        raise DeserializationError("DescribeLogPatternRequest.pattern_name required")
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    return out

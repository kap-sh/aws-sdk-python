"""Generated from Smithy shape ``com.amazonaws.networkfirewall#SourceMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.resource_arn
    import aws_sdk_network_firewall.types.update_token


class SourceMetadata(TypedDict):
    source_arn: NotRequired["aws_sdk_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the rule group that your own rule group is copied from.</p>"""
    source_update_token: NotRequired[
        "aws_sdk_network_firewall.types.update_token.UpdateToken"
    ]
    """<p>The update token of the Amazon Web Services managed rule group that your own rule group is copied from. To determine the update token for the managed rule group, call <a href=\"https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DescribeRuleGroup.html#networkfirewall-DescribeRuleGroup-response-UpdateToken\">DescribeRuleGroup</a>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SourceMetadata) -> dict:
    out: dict = {}
    if "source_arn" in value:
        out["SourceArn"] = value["source_arn"]
    if "source_update_token" in value:
        out["SourceUpdateToken"] = value["source_update_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SourceMetadata:
    out: SourceMetadata = {}  # type: ignore[typeddict-item]
    if "SourceArn" in data:
        out["source_arn"] = data["SourceArn"]
    if "SourceUpdateToken" in data:
        out["source_update_token"] = data["SourceUpdateToken"]
    return out

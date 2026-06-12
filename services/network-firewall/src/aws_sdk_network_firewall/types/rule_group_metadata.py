"""Generated from Smithy shape ``com.amazonaws.networkfirewall#RuleGroupMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.resource_arn
    import aws_sdk_network_firewall.types.resource_name
    import aws_sdk_network_firewall.types.vendor_name


class RuleGroupMetadata(TypedDict):
    name: NotRequired["aws_sdk_network_firewall.types.resource_name.ResourceName"]
    """<p>The descriptive name of the rule group. You can't change the name of a rule group after you create it.</p>"""
    arn: NotRequired["aws_sdk_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the rule group.</p>"""
    vendor_name: NotRequired["aws_sdk_network_firewall.types.vendor_name.VendorName"]
    """<p>The name of the Amazon Web Services Marketplace seller that provides this rule group.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleGroupMetadata) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "vendor_name" in value:
        out["VendorName"] = value["vendor_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RuleGroupMetadata:
    out: RuleGroupMetadata = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "VendorName" in data:
        out["vendor_name"] = data["VendorName"]
    return out

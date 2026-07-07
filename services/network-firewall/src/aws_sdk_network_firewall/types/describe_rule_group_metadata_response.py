"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DescribeRuleGroupMetadataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.description
    import aws_sdk_network_firewall.types.last_update_time
    import aws_sdk_network_firewall.types.listing_name
    import aws_sdk_network_firewall.types.product_id
    import aws_sdk_network_firewall.types.resource_arn
    import aws_sdk_network_firewall.types.resource_name
    import aws_sdk_network_firewall.types.rule_capacity
    import aws_sdk_network_firewall.types.rule_group_type
    import aws_sdk_network_firewall.types.stateful_rule_options
    import aws_sdk_network_firewall.types.vendor_name


class DescribeRuleGroupMetadataResponse(TypedDict, closed=True):
    rule_group_arn: "aws_sdk_network_firewall.types.resource_arn.ResourceArn"
    """<p>The descriptive name of the rule group. You can't change the name of a rule group after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    rule_group_name: "aws_sdk_network_firewall.types.resource_name.ResourceName"
    """<p>The descriptive name of the rule group. You can't change the name of a rule group after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    description: NotRequired["aws_sdk_network_firewall.types.description.Description"]
    """<p>Returns the metadata objects for the specified rule group. </p>"""
    type: NotRequired["aws_sdk_network_firewall.types.rule_group_type.RuleGroupType"]
    """<p>Indicates whether the rule group is stateless or stateful. If the rule group is stateless, it contains stateless rules. If it is stateful, it contains stateful rules. </p> <note> <p>This setting is required for requests that do not include the <code>RuleGroupARN</code>.</p> </note>"""
    capacity: NotRequired["aws_sdk_network_firewall.types.rule_capacity.RuleCapacity"]
    """<p>The maximum operating resources that this rule group can use. Rule group capacity is fixed at creation. When you update a rule group, you are limited to this capacity. When you reference a rule group from a firewall policy, Network Firewall reserves this capacity for the rule group. </p> <p>You can retrieve the capacity that would be required for a rule group before you create the rule group by calling <a>CreateRuleGroup</a> with <code>DryRun</code> set to <code>TRUE</code>. </p>"""
    stateful_rule_options: NotRequired[
        "aws_sdk_network_firewall.types.stateful_rule_options.StatefulRuleOptions"
    ]
    last_modified_time: NotRequired[
        "aws_sdk_network_firewall.types.last_update_time.LastUpdateTime"
    ]
    """<p>A timestamp indicating when the rule group was last modified.</p>"""
    vendor_name: NotRequired["aws_sdk_network_firewall.types.vendor_name.VendorName"]
    """<p>The name of the Amazon Web Services Marketplace vendor that provides this rule group.</p>"""
    product_id: NotRequired["aws_sdk_network_firewall.types.product_id.ProductId"]
    """<p>The unique identifier for the product listing associated with this rule group.</p>"""
    listing_name: NotRequired["aws_sdk_network_firewall.types.listing_name.ListingName"]
    """<p>The display name of the product listing for this rule group.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeRuleGroupMetadataResponse) -> dict:
    out: dict = {}
    out["RuleGroupArn"] = value["rule_group_arn"]
    out["RuleGroupName"] = value["rule_group_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "type" in value:
        import aws_sdk_network_firewall.types.rule_group_type

        out["Type"] = (
            aws_sdk_network_firewall.types.rule_group_type.serialize_aws_json_1_0(
                value["type"]
            )
        )
    if "capacity" in value:
        out["Capacity"] = value["capacity"]
    if "stateful_rule_options" in value:
        import aws_sdk_network_firewall.types.stateful_rule_options

        out["StatefulRuleOptions"] = (
            aws_sdk_network_firewall.types.stateful_rule_options.serialize_aws_json_1_0(
                value["stateful_rule_options"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_network_firewall.types.last_update_time

        out["LastModifiedTime"] = (
            aws_sdk_network_firewall.types.last_update_time.serialize_aws_json_1_0(
                value["last_modified_time"]
            )
        )
    if "vendor_name" in value:
        out["VendorName"] = value["vendor_name"]
    if "product_id" in value:
        out["ProductId"] = value["product_id"]
    if "listing_name" in value:
        out["ListingName"] = value["listing_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeRuleGroupMetadataResponse:
    out: DescribeRuleGroupMetadataResponse = {}  # type: ignore[typeddict-item]
    if "RuleGroupArn" in data:
        out["rule_group_arn"] = data["RuleGroupArn"]
    else:
        raise DeserializationError(
            "DescribeRuleGroupMetadataResponse.rule_group_arn required"
        )
    if "RuleGroupName" in data:
        out["rule_group_name"] = data["RuleGroupName"]
    else:
        raise DeserializationError(
            "DescribeRuleGroupMetadataResponse.rule_group_name required"
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Type" in data:
        import aws_sdk_network_firewall.types.rule_group_type

        out["type"] = (
            aws_sdk_network_firewall.types.rule_group_type.deserialize_aws_json_1_0(
                data["Type"]
            )
        )
    if "Capacity" in data:
        out["capacity"] = data["Capacity"]
    if "StatefulRuleOptions" in data:
        import aws_sdk_network_firewall.types.stateful_rule_options

        out["stateful_rule_options"] = (
            aws_sdk_network_firewall.types.stateful_rule_options.deserialize_aws_json_1_0(
                data["StatefulRuleOptions"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_network_firewall.types.last_update_time

        out["last_modified_time"] = (
            aws_sdk_network_firewall.types.last_update_time.deserialize_aws_json_1_0(
                data["LastModifiedTime"]
            )
        )
    if "VendorName" in data:
        out["vendor_name"] = data["VendorName"]
    if "ProductId" in data:
        out["product_id"] = data["ProductId"]
    if "ListingName" in data:
        out["listing_name"] = data["ListingName"]
    return out

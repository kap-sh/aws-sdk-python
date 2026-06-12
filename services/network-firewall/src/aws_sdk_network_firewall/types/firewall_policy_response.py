"""Generated from Smithy shape ``com.amazonaws.networkfirewall#FirewallPolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.description
    import aws_sdk_network_firewall.types.encryption_configuration
    import aws_sdk_network_firewall.types.last_update_time
    import aws_sdk_network_firewall.types.number_of_associations
    import aws_sdk_network_firewall.types.resource_arn
    import aws_sdk_network_firewall.types.resource_id
    import aws_sdk_network_firewall.types.resource_name
    import aws_sdk_network_firewall.types.resource_status
    import aws_sdk_network_firewall.types.rule_capacity
    import aws_sdk_network_firewall.types.tag_list


class FirewallPolicyResponse(TypedDict):
    firewall_policy_name: "aws_sdk_network_firewall.types.resource_name.ResourceName"
    """<p>The descriptive name of the firewall policy. You can't change the name of a firewall policy after you create it.</p>"""
    firewall_policy_arn: "aws_sdk_network_firewall.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the firewall policy.</p> <note> <p>If this response is for a create request that had <code>DryRun</code> set to <code>TRUE</code>, then this ARN is a placeholder that isn't attached to a valid resource.</p> </note>"""
    firewall_policy_id: "aws_sdk_network_firewall.types.resource_id.ResourceId"
    """<p>The unique identifier for the firewall policy. </p>"""
    description: NotRequired["aws_sdk_network_firewall.types.description.Description"]
    """<p>A description of the firewall policy.</p>"""
    firewall_policy_status: NotRequired[
        "aws_sdk_network_firewall.types.resource_status.ResourceStatus"
    ]
    """<p>The current status of the firewall policy. You can retrieve this for a firewall policy by calling <a>DescribeFirewallPolicy</a> and providing the firewall policy's name or ARN.</p>"""
    tags: NotRequired["aws_sdk_network_firewall.types.tag_list.TagList"]
    """<p>The key:value pairs to associate with the resource.</p>"""
    consumed_stateless_rule_capacity: NotRequired[
        "aws_sdk_network_firewall.types.rule_capacity.RuleCapacity"
    ]
    """<p>The number of capacity units currently consumed by the policy's stateless rules.</p>"""
    consumed_stateful_rule_capacity: NotRequired[
        "aws_sdk_network_firewall.types.rule_capacity.RuleCapacity"
    ]
    """<p>The number of capacity units currently consumed by the policy's stateful rules.</p>"""
    consumed_stateful_domain_capacity: NotRequired[
        "aws_sdk_network_firewall.types.rule_capacity.RuleCapacity"
    ]
    """<p>The total number of domain name specifications across all domain list rule groups in the firewall policy that use the <code>stateful-domain-rulegroup</code> resource type.</p>"""
    number_of_associations: NotRequired[
        "aws_sdk_network_firewall.types.number_of_associations.NumberOfAssociations"
    ]
    """<p>The number of firewalls that are associated with this firewall policy.</p>"""
    encryption_configuration: NotRequired[
        "aws_sdk_network_firewall.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>A complex type that contains the Amazon Web Services KMS encryption configuration settings for your firewall policy.</p>"""
    last_modified_time: NotRequired[
        "aws_sdk_network_firewall.types.last_update_time.LastUpdateTime"
    ]
    """<p>The last time that the firewall policy was changed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FirewallPolicyResponse) -> dict:
    out: dict = {}
    out["FirewallPolicyName"] = value["firewall_policy_name"]
    out["FirewallPolicyArn"] = value["firewall_policy_arn"]
    out["FirewallPolicyId"] = value["firewall_policy_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "firewall_policy_status" in value:
        import aws_sdk_network_firewall.types.resource_status

        out["FirewallPolicyStatus"] = (
            aws_sdk_network_firewall.types.resource_status.serialize_aws_json_1_0(
                value["firewall_policy_status"]
            )
        )
    if "tags" in value:
        import aws_sdk_network_firewall.types.tag_list

        out["Tags"] = aws_sdk_network_firewall.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "consumed_stateless_rule_capacity" in value:
        out["ConsumedStatelessRuleCapacity"] = value["consumed_stateless_rule_capacity"]
    if "consumed_stateful_rule_capacity" in value:
        out["ConsumedStatefulRuleCapacity"] = value["consumed_stateful_rule_capacity"]
    if "consumed_stateful_domain_capacity" in value:
        out["ConsumedStatefulDomainCapacity"] = value[
            "consumed_stateful_domain_capacity"
        ]
    if "number_of_associations" in value:
        out["NumberOfAssociations"] = value["number_of_associations"]
    if "encryption_configuration" in value:
        import aws_sdk_network_firewall.types.encryption_configuration

        out["EncryptionConfiguration"] = (
            aws_sdk_network_firewall.types.encryption_configuration.serialize_aws_json_1_0(
                value["encryption_configuration"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_network_firewall.types.last_update_time

        out["LastModifiedTime"] = (
            aws_sdk_network_firewall.types.last_update_time.serialize_aws_json_1_0(
                value["last_modified_time"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> FirewallPolicyResponse:
    out: FirewallPolicyResponse = {}  # type: ignore[typeddict-item]
    if "FirewallPolicyName" in data:
        out["firewall_policy_name"] = data["FirewallPolicyName"]
    else:
        raise DeserializationError(
            "FirewallPolicyResponse.firewall_policy_name required"
        )
    if "FirewallPolicyArn" in data:
        out["firewall_policy_arn"] = data["FirewallPolicyArn"]
    else:
        raise DeserializationError(
            "FirewallPolicyResponse.firewall_policy_arn required"
        )
    if "FirewallPolicyId" in data:
        out["firewall_policy_id"] = data["FirewallPolicyId"]
    else:
        raise DeserializationError("FirewallPolicyResponse.firewall_policy_id required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "FirewallPolicyStatus" in data:
        import aws_sdk_network_firewall.types.resource_status

        out["firewall_policy_status"] = (
            aws_sdk_network_firewall.types.resource_status.deserialize_aws_json_1_0(
                data["FirewallPolicyStatus"]
            )
        )
    if "Tags" in data:
        import aws_sdk_network_firewall.types.tag_list

        out["tags"] = aws_sdk_network_firewall.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    if "ConsumedStatelessRuleCapacity" in data:
        out["consumed_stateless_rule_capacity"] = data["ConsumedStatelessRuleCapacity"]
    if "ConsumedStatefulRuleCapacity" in data:
        out["consumed_stateful_rule_capacity"] = data["ConsumedStatefulRuleCapacity"]
    if "ConsumedStatefulDomainCapacity" in data:
        out["consumed_stateful_domain_capacity"] = data[
            "ConsumedStatefulDomainCapacity"
        ]
    if "NumberOfAssociations" in data:
        out["number_of_associations"] = data["NumberOfAssociations"]
    if "EncryptionConfiguration" in data:
        import aws_sdk_network_firewall.types.encryption_configuration

        out["encryption_configuration"] = (
            aws_sdk_network_firewall.types.encryption_configuration.deserialize_aws_json_1_0(
                data["EncryptionConfiguration"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_network_firewall.types.last_update_time

        out["last_modified_time"] = (
            aws_sdk_network_firewall.types.last_update_time.deserialize_aws_json_1_0(
                data["LastModifiedTime"]
            )
        )
    return out

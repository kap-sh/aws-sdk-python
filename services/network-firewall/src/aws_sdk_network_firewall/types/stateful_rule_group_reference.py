"""Generated from Smithy shape ``com.amazonaws.networkfirewall#StatefulRuleGroupReference``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.deep_threat_inspection
    import aws_sdk_network_firewall.types.priority
    import aws_sdk_network_firewall.types.resource_arn
    import aws_sdk_network_firewall.types.stateful_rule_group_override


class StatefulRuleGroupReference(TypedDict):
    resource_arn: "aws_sdk_network_firewall.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the stateful rule group.</p>"""
    priority: NotRequired["aws_sdk_network_firewall.types.priority.Priority"]
    """<p>An integer setting that indicates the order in which to run the stateful rule groups in a single <a>FirewallPolicy</a>. This setting only applies to firewall policies that specify the <code>STRICT_ORDER</code> rule order in the stateful engine options settings.</p> <p>Network Firewall evalutes each stateful rule group against a packet starting with the group that has the lowest priority setting. You must ensure that the priority settings are unique within each policy.</p> <p>You can change the priority settings of your rule groups at any time. To make it easier to insert rule groups later, number them so there's a wide range in between, for example use 100, 200, and so on. </p>"""
    override: NotRequired[
        "aws_sdk_network_firewall.types.stateful_rule_group_override.StatefulRuleGroupOverride"
    ]
    """<p>The action that allows the policy owner to override the behavior of the rule group within a policy.</p>"""
    deep_threat_inspection: NotRequired[
        "aws_sdk_network_firewall.types.deep_threat_inspection.DeepThreatInspection"
    ]
    """<p>Network Firewall plans to augment the active threat defense managed rule group with an additional deep threat inspection capability. When this capability is released, Amazon Web Services will analyze service logs of network traffic processed by these rule groups to identify threat indicators across customers. Amazon Web Services will use these threat indicators to improve the active threat defense managed rule groups and protect the security of Amazon Web Services customers and services.</p> <note> <p>Customers can opt-out of deep threat inspection at any time through the Network Firewall console or API. When customers opt out, Network Firewall will not use the network traffic processed by those customers' active threat defense rule groups for rule group improvement.</p> </note>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StatefulRuleGroupReference) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    if "priority" in value:
        out["Priority"] = value["priority"]
    if "override" in value:
        import aws_sdk_network_firewall.types.stateful_rule_group_override

        out["Override"] = (
            aws_sdk_network_firewall.types.stateful_rule_group_override.serialize_aws_json_1_0(
                value["override"]
            )
        )
    if "deep_threat_inspection" in value:
        out["DeepThreatInspection"] = value["deep_threat_inspection"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StatefulRuleGroupReference:
    out: StatefulRuleGroupReference = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("StatefulRuleGroupReference.resource_arn required")
    if "Priority" in data:
        out["priority"] = data["Priority"]
    if "Override" in data:
        import aws_sdk_network_firewall.types.stateful_rule_group_override

        out["override"] = (
            aws_sdk_network_firewall.types.stateful_rule_group_override.deserialize_aws_json_1_0(
                data["Override"]
            )
        )
    if "DeepThreatInspection" in data:
        out["deep_threat_inspection"] = data["DeepThreatInspection"]
    return out

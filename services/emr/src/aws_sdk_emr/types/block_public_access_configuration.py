"""Generated from Smithy shape ``com.amazonaws.emr#BlockPublicAccessConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.boolean
    import aws_sdk_emr.types.configuration_list
    import aws_sdk_emr.types.port_ranges
    import aws_sdk_emr.types.string
    import aws_sdk_emr.types.string_map


class BlockPublicAccessConfiguration(TypedDict):
    block_public_security_group_rules: NotRequired["aws_sdk_emr.types.boolean.Boolean"]
    """<p>Indicates whether Amazon EMR block public access is enabled (<code>true</code>) or disabled (<code>false</code>). By default, the value is <code>false</code> for accounts that have created Amazon EMR clusters before July 2019. For accounts created after this, the default is <code>true</code>.</p>"""
    permitted_public_security_group_rule_ranges: NotRequired[
        "aws_sdk_emr.types.port_ranges.PortRanges"
    ]
    """<p>Specifies ports and port ranges that are permitted to have security group rules that allow inbound traffic from all public sources. For example, if Port 23 (Telnet) is specified for <code>PermittedPublicSecurityGroupRuleRanges</code>, Amazon EMR allows cluster creation if a security group associated with the cluster has a rule that allows inbound traffic on Port 23 from IPv4 0.0.0.0/0 or IPv6 port ::/0 as the source.</p> <p>By default, Port 22, which is used for SSH access to the cluster Amazon EC2 instances, is in the list of <code>PermittedPublicSecurityGroupRuleRanges</code>.</p>"""
    classification: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The classification within a configuration.</p>"""
    configurations: NotRequired[
        "aws_sdk_emr.types.configuration_list.ConfigurationList"
    ]
    """<p>A list of additional configurations to apply within a configuration object.</p>"""
    properties: NotRequired["aws_sdk_emr.types.string_map.StringMap"]
    """<p>A set of properties specified within a configuration classification.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BlockPublicAccessConfiguration) -> dict:
    out: dict = {}
    if "block_public_security_group_rules" in value:
        out["BlockPublicSecurityGroupRules"] = value[
            "block_public_security_group_rules"
        ]
    if "permitted_public_security_group_rule_ranges" in value:
        import aws_sdk_emr.types.port_ranges

        out["PermittedPublicSecurityGroupRuleRanges"] = (
            aws_sdk_emr.types.port_ranges.serialize_aws_json_1_1(
                value["permitted_public_security_group_rule_ranges"]
            )
        )
    if "classification" in value:
        out["Classification"] = value["classification"]
    if "configurations" in value:
        import aws_sdk_emr.types.configuration_list

        out["Configurations"] = (
            aws_sdk_emr.types.configuration_list.serialize_aws_json_1_1(
                value["configurations"]
            )
        )
    if "properties" in value:
        import aws_sdk_emr.types.string_map

        out["Properties"] = aws_sdk_emr.types.string_map.serialize_aws_json_1_1(
            value["properties"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BlockPublicAccessConfiguration:
    out: BlockPublicAccessConfiguration = {}  # type: ignore[typeddict-item]
    if "BlockPublicSecurityGroupRules" in data:
        out["block_public_security_group_rules"] = data["BlockPublicSecurityGroupRules"]
    if "PermittedPublicSecurityGroupRuleRanges" in data:
        import aws_sdk_emr.types.port_ranges

        out["permitted_public_security_group_rule_ranges"] = (
            aws_sdk_emr.types.port_ranges.deserialize_aws_json_1_1(
                data["PermittedPublicSecurityGroupRuleRanges"]
            )
        )
    if "Classification" in data:
        out["classification"] = data["Classification"]
    if "Configurations" in data:
        import aws_sdk_emr.types.configuration_list

        out["configurations"] = (
            aws_sdk_emr.types.configuration_list.deserialize_aws_json_1_1(
                data["Configurations"]
            )
        )
    if "Properties" in data:
        import aws_sdk_emr.types.string_map

        out["properties"] = aws_sdk_emr.types.string_map.deserialize_aws_json_1_1(
            data["Properties"]
        )
    return out

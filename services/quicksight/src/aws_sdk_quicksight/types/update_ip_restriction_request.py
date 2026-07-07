"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateIpRestrictionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.ip_restriction_rule_map
    import aws_sdk_quicksight.types.nullable_boolean
    import aws_sdk_quicksight.types.vpc_endpoint_id_restriction_rule_map
    import aws_sdk_quicksight.types.vpc_id_restriction_rule_map


class UpdateIpRestrictionRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the IP rules.</p>"""
    ip_restriction_rule_map: NotRequired[
        "aws_sdk_quicksight.types.ip_restriction_rule_map.IpRestrictionRuleMap"
    ]
    """<p>A map that describes the updated IP rules with CIDR ranges and descriptions.</p>"""
    vpc_id_restriction_rule_map: NotRequired[
        "aws_sdk_quicksight.types.vpc_id_restriction_rule_map.VpcIdRestrictionRuleMap"
    ]
    """<p>A map of VPC IDs and their corresponding rules. When you configure this parameter, traffic from all VPC endpoints that are present in the specified VPC is allowed.</p>"""
    vpc_endpoint_id_restriction_rule_map: NotRequired[
        "aws_sdk_quicksight.types.vpc_endpoint_id_restriction_rule_map.VpcEndpointIdRestrictionRuleMap"
    ]
    """<p>A map of allowed VPC endpoint IDs and their corresponding rule descriptions.</p>"""
    enabled: NotRequired["aws_sdk_quicksight.types.nullable_boolean.NullableBoolean"]
    """<p>A value that specifies whether IP rules are turned on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIpRestrictionRequest) -> dict:
    out: dict = {}
    if "ip_restriction_rule_map" in value:
        import aws_sdk_quicksight.types.ip_restriction_rule_map

        out["IpRestrictionRuleMap"] = (
            aws_sdk_quicksight.types.ip_restriction_rule_map.serialize_json(
                value["ip_restriction_rule_map"]
            )
        )
    if "vpc_id_restriction_rule_map" in value:
        import aws_sdk_quicksight.types.vpc_id_restriction_rule_map

        out["VpcIdRestrictionRuleMap"] = (
            aws_sdk_quicksight.types.vpc_id_restriction_rule_map.serialize_json(
                value["vpc_id_restriction_rule_map"]
            )
        )
    if "vpc_endpoint_id_restriction_rule_map" in value:
        import aws_sdk_quicksight.types.vpc_endpoint_id_restriction_rule_map

        out["VpcEndpointIdRestrictionRuleMap"] = (
            aws_sdk_quicksight.types.vpc_endpoint_id_restriction_rule_map.serialize_json(
                value["vpc_endpoint_id_restriction_rule_map"]
            )
        )
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> UpdateIpRestrictionRequest:
    out: UpdateIpRestrictionRequest = {}  # type: ignore[typeddict-item]
    if "IpRestrictionRuleMap" in data:
        import aws_sdk_quicksight.types.ip_restriction_rule_map

        out["ip_restriction_rule_map"] = (
            aws_sdk_quicksight.types.ip_restriction_rule_map.deserialize_json(
                data["IpRestrictionRuleMap"]
            )
        )
    if "VpcIdRestrictionRuleMap" in data:
        import aws_sdk_quicksight.types.vpc_id_restriction_rule_map

        out["vpc_id_restriction_rule_map"] = (
            aws_sdk_quicksight.types.vpc_id_restriction_rule_map.deserialize_json(
                data["VpcIdRestrictionRuleMap"]
            )
        )
    if "VpcEndpointIdRestrictionRuleMap" in data:
        import aws_sdk_quicksight.types.vpc_endpoint_id_restriction_rule_map

        out["vpc_endpoint_id_restriction_rule_map"] = (
            aws_sdk_quicksight.types.vpc_endpoint_id_restriction_rule_map.deserialize_json(
                data["VpcEndpointIdRestrictionRuleMap"]
            )
        )
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    return out

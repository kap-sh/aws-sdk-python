"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeIpRestrictionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.ip_restriction_rule_map
    import capo_quicksight.types.nullable_boolean
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string
    import capo_quicksight.types.vpc_endpoint_id_restriction_rule_map
    import capo_quicksight.types.vpc_id_restriction_rule_map


class DescribeIpRestrictionResponse(TypedDict, closed=True):
    aws_account_id: NotRequired["capo_quicksight.types.aws_account_id.AwsAccountId"]
    """<p>The ID of the Amazon Web Services account that contains the IP rules.</p>"""
    ip_restriction_rule_map: NotRequired[
        "capo_quicksight.types.ip_restriction_rule_map.IpRestrictionRuleMap"
    ]
    """<p>A map that describes the IP rules with CIDR range and description.</p>"""
    vpc_id_restriction_rule_map: NotRequired[
        "capo_quicksight.types.vpc_id_restriction_rule_map.VpcIdRestrictionRuleMap"
    ]
    """<p>A map of allowed VPC IDs and their rule descriptions.</p>"""
    vpc_endpoint_id_restriction_rule_map: NotRequired[
        "capo_quicksight.types.vpc_endpoint_id_restriction_rule_map.VpcEndpointIdRestrictionRuleMap"
    ]
    """<p>A map of allowed VPC endpoint IDs and their rule descriptions.</p>"""
    enabled: NotRequired["capo_quicksight.types.nullable_boolean.NullableBoolean"]
    """<p>A value that specifies whether IP rules are turned on.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeIpRestrictionResponse) -> dict:
    out: dict = {}
    if "aws_account_id" in value:
        out["AwsAccountId"] = value["aws_account_id"]
    if "ip_restriction_rule_map" in value:
        import capo_quicksight.types.ip_restriction_rule_map

        out["IpRestrictionRuleMap"] = (
            capo_quicksight.types.ip_restriction_rule_map.serialize_json(
                value["ip_restriction_rule_map"]
            )
        )
    if "vpc_id_restriction_rule_map" in value:
        import capo_quicksight.types.vpc_id_restriction_rule_map

        out["VpcIdRestrictionRuleMap"] = (
            capo_quicksight.types.vpc_id_restriction_rule_map.serialize_json(
                value["vpc_id_restriction_rule_map"]
            )
        )
    if "vpc_endpoint_id_restriction_rule_map" in value:
        import capo_quicksight.types.vpc_endpoint_id_restriction_rule_map

        out["VpcEndpointIdRestrictionRuleMap"] = (
            capo_quicksight.types.vpc_endpoint_id_restriction_rule_map.serialize_json(
                value["vpc_endpoint_id_restriction_rule_map"]
            )
        )
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeIpRestrictionResponse:
    out: DescribeIpRestrictionResponse = {}  # type: ignore[typeddict-item]
    if "AwsAccountId" in data:
        out["aws_account_id"] = data["AwsAccountId"]
    if "IpRestrictionRuleMap" in data:
        import capo_quicksight.types.ip_restriction_rule_map

        out["ip_restriction_rule_map"] = (
            capo_quicksight.types.ip_restriction_rule_map.deserialize_json(
                data["IpRestrictionRuleMap"]
            )
        )
    if "VpcIdRestrictionRuleMap" in data:
        import capo_quicksight.types.vpc_id_restriction_rule_map

        out["vpc_id_restriction_rule_map"] = (
            capo_quicksight.types.vpc_id_restriction_rule_map.deserialize_json(
                data["VpcIdRestrictionRuleMap"]
            )
        )
    if "VpcEndpointIdRestrictionRuleMap" in data:
        import capo_quicksight.types.vpc_endpoint_id_restriction_rule_map

        out["vpc_endpoint_id_restriction_rule_map"] = (
            capo_quicksight.types.vpc_endpoint_id_restriction_rule_map.deserialize_json(
                data["VpcEndpointIdRestrictionRuleMap"]
            )
        )
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out

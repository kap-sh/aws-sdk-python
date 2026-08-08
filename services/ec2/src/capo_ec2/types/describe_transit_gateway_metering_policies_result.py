"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTransitGatewayMeteringPoliciesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.transit_gateway_metering_policy_list


class DescribeTransitGatewayMeteringPoliciesResult(TypedDict, closed=True):
    transit_gateway_metering_policies: NotRequired[
        "capo_ec2.types.transit_gateway_metering_policy_list.TransitGatewayMeteringPolicyList"
    ]
    """<p>Information about the transit gateway metering policies.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeTransitGatewayMeteringPoliciesResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transit_gateway_metering_policies" in value:
        import capo_ec2.types.transit_gateway_metering_policy_list

        capo_ec2.types.transit_gateway_metering_policy_list.serialize_ec2_query(
            value["transit_gateway_metering_policies"],
            pairs,
            f"{key_prefix}TransitGatewayMeteringPolicies",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeTransitGatewayMeteringPoliciesResult:
    out: DescribeTransitGatewayMeteringPoliciesResult = {}  # type: ignore[typeddict-item]
    if el.find("transitGatewayMeteringPolicies") is not None:
        import capo_ec2.types.transit_gateway_metering_policy_list

        out["transit_gateway_metering_policies"] = (
            capo_ec2.types.transit_gateway_metering_policy_list.deserialize_ec2_query(
                el, "transitGatewayMeteringPolicies"
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out

"""Generated from Smithy shape ``com.amazonaws.ec2#GetCoipPoolUsageResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.coip_address_usage_set
    import capo_ec2.types.string


class GetCoipPoolUsageResult(TypedDict, closed=True):
    coip_pool_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the customer-owned address pool.</p>"""
    coip_address_usages: NotRequired[
        "capo_ec2.types.coip_address_usage_set.CoipAddressUsageSet"
    ]
    """<p>Information about the address usage.</p>"""
    local_gateway_route_table_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the local gateway route table.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetCoipPoolUsageResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "coip_pool_id" in value:
        pairs.append((f"{prefix}.CoipPoolId", str(value["coip_pool_id"])))
    if "coip_address_usages" in value:
        import capo_ec2.types.coip_address_usage_set

        capo_ec2.types.coip_address_usage_set.serialize_ec2_query(
            value["coip_address_usages"], pairs, f"{prefix}.CoipAddressUsageSet"
        )
    if "local_gateway_route_table_id" in value:
        pairs.append(
            (
                f"{prefix}.LocalGatewayRouteTableId",
                str(value["local_gateway_route_table_id"]),
            )
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetCoipPoolUsageResult:
    out: GetCoipPoolUsageResult = {}  # type: ignore[typeddict-item]
    child_coip_pool_id = el.find("CoipPoolId")
    if child_coip_pool_id is not None:
        out["coip_pool_id"] = str(child_coip_pool_id.text or "")
    if el.find("CoipAddressUsageSet") is not None:
        import capo_ec2.types.coip_address_usage_set

        out["coip_address_usages"] = (
            capo_ec2.types.coip_address_usage_set.deserialize_ec2_query(
                el, "CoipAddressUsageSet"
            )
        )
    child_local_gateway_route_table_id = el.find("LocalGatewayRouteTableId")
    if child_local_gateway_route_table_id is not None:
        out["local_gateway_route_table_id"] = str(
            child_local_gateway_route_table_id.text or ""
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out

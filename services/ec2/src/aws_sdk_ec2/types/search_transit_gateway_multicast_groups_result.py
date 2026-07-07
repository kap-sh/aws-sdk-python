"""Generated from Smithy shape ``com.amazonaws.ec2#SearchTransitGatewayMulticastGroupsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_multicast_group_list


class SearchTransitGatewayMulticastGroupsResult(TypedDict, closed=True):
    multicast_groups: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_multicast_group_list.TransitGatewayMulticastGroupList"
    ]
    """<p>Information about the transit gateway multicast group.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SearchTransitGatewayMulticastGroupsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "multicast_groups" in value:
        import aws_sdk_ec2.types.transit_gateway_multicast_group_list

        aws_sdk_ec2.types.transit_gateway_multicast_group_list.serialize_ec2_query(
            value["multicast_groups"], pairs, f"{prefix}.MulticastGroups"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> SearchTransitGatewayMulticastGroupsResult:
    out: SearchTransitGatewayMulticastGroupsResult = {}  # type: ignore[typeddict-item]
    if el.find("MulticastGroups") is not None:
        import aws_sdk_ec2.types.transit_gateway_multicast_group_list

        out["multicast_groups"] = (
            aws_sdk_ec2.types.transit_gateway_multicast_group_list.deserialize_ec2_query(
                el, "MulticastGroups"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out

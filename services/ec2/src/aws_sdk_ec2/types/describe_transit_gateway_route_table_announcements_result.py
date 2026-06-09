"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTransitGatewayRouteTableAnnouncementsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_route_table_announcement_list


class DescribeTransitGatewayRouteTableAnnouncementsResult(TypedDict):
    transit_gateway_route_table_announcements: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_route_table_announcement_list.TransitGatewayRouteTableAnnouncementList"
    ]
    """<p>Describes the transit gateway route table announcement.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token for the next page of results.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeTransitGatewayRouteTableAnnouncementsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "transit_gateway_route_table_announcements" in value:
        import aws_sdk_ec2.types.transit_gateway_route_table_announcement_list

        aws_sdk_ec2.types.transit_gateway_route_table_announcement_list.serialize_ec2_query(
            value["transit_gateway_route_table_announcements"],
            pairs,
            f"{prefix}.TransitGatewayRouteTableAnnouncements",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(
    el: Element,
) -> DescribeTransitGatewayRouteTableAnnouncementsResult:
    out: DescribeTransitGatewayRouteTableAnnouncementsResult = {}  # type: ignore[typeddict-item]
    if el.find("TransitGatewayRouteTableAnnouncements") is not None:
        import aws_sdk_ec2.types.transit_gateway_route_table_announcement_list

        out["transit_gateway_route_table_announcements"] = (
            aws_sdk_ec2.types.transit_gateway_route_table_announcement_list.deserialize_ec2_query(
                el, "TransitGatewayRouteTableAnnouncements"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out

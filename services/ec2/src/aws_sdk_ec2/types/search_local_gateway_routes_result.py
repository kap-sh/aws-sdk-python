"""Generated from Smithy shape ``com.amazonaws.ec2#SearchLocalGatewayRoutesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_gateway_route_list
    import aws_sdk_ec2.types.string


class SearchLocalGatewayRoutesResult(TypedDict, closed=True):
    routes: NotRequired[
        "aws_sdk_ec2.types.local_gateway_route_list.LocalGatewayRouteList"
    ]
    """<p>Information about the routes.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SearchLocalGatewayRoutesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "routes" in value:
        import aws_sdk_ec2.types.local_gateway_route_list

        aws_sdk_ec2.types.local_gateway_route_list.serialize_ec2_query(
            value["routes"], pairs, f"{prefix}.RouteSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> SearchLocalGatewayRoutesResult:
    out: SearchLocalGatewayRoutesResult = {}  # type: ignore[typeddict-item]
    if el.find("RouteSet") is not None:
        import aws_sdk_ec2.types.local_gateway_route_list

        out["routes"] = (
            aws_sdk_ec2.types.local_gateway_route_list.deserialize_ec2_query(
                el, "RouteSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out

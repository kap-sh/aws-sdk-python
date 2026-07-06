"""Generated from Smithy shape ``com.amazonaws.ec2#ExportTransitGatewayRoutesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_route_table_id


class ExportTransitGatewayRoutesRequest(TypedDict, closed=True):
    transit_gateway_route_table_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_route_table_id.TransitGatewayRouteTableId"
    ]
    """<p>The ID of the route table.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters. The possible values are:</p> <ul> <li> <p> <code>attachment.transit-gateway-attachment-id</code> - The id of the transit gateway attachment.</p> </li> <li> <p> <code>attachment.resource-id</code> - The resource id of the transit gateway attachment.</p> </li> <li> <p> <code>route-search.exact-match</code> - The exact match of the specified filter.</p> </li> <li> <p> <code>route-search.longest-prefix-match</code> - The longest prefix that matches the route.</p> </li> <li> <p> <code>route-search.subnet-of-match</code> - The routes with a subnet that match the specified CIDR filter.</p> </li> <li> <p> <code>route-search.supernet-of-match</code> - The routes with a CIDR that encompass the CIDR filter. For example, if you have 10.0.1.0/29 and 10.0.1.0/31 routes in your route table and you specify supernet-of-match as 10.0.1.0/30, then the result returns 10.0.1.0/29.</p> </li> <li> <p> <code>state</code> - The state of the route (<code>active</code> | <code>blackhole</code>).</p> </li> <li> <p> <code>transit-gateway-route-destination-cidr-block</code> - The CIDR range.</p> </li> <li> <p> <code>type</code> - The type of route (<code>propagated</code> | <code>static</code>).</p> </li> </ul>"""
    s3_bucket: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the S3 bucket.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ExportTransitGatewayRoutesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "transit_gateway_route_table_id" in value:
        pairs.append(
            (
                f"{prefix}.TransitGatewayRouteTableId",
                str(value["transit_gateway_route_table_id"]),
            )
        )
    if "filters" in value:
        import aws_sdk_ec2.types.filter_list

        aws_sdk_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "s3_bucket" in value:
        pairs.append((f"{prefix}.S3Bucket", str(value["s3_bucket"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> ExportTransitGatewayRoutesRequest:
    out: ExportTransitGatewayRoutesRequest = {}  # type: ignore[typeddict-item]
    child_transit_gateway_route_table_id = el.find("TransitGatewayRouteTableId")
    if child_transit_gateway_route_table_id is not None:
        out["transit_gateway_route_table_id"] = str(
            child_transit_gateway_route_table_id.text or ""
        )
    if el.find("Filters") is not None:
        import aws_sdk_ec2.types.filter_list

        out["filters"] = aws_sdk_ec2.types.filter_list.deserialize_ec2_query(
            el, "Filters"
        )
    child_s3_bucket = el.find("S3Bucket")
    if child_s3_bucket is not None:
        out["s3_bucket"] = str(child_s3_bucket.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out

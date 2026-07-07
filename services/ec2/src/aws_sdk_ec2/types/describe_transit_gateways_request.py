"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTransitGatewaysRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_id_string_list
    import aws_sdk_ec2.types.transit_gateway_max_results


class DescribeTransitGatewaysRequest(TypedDict, closed=True):
    transit_gateway_ids: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_id_string_list.TransitGatewayIdStringList"
    ]
    """<p>The IDs of the transit gateways.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters. The possible values are:</p> <ul> <li> <p> <code>options.propagation-default-route-table-id</code> - The ID of the default propagation route table.</p> </li> <li> <p> <code>options.amazon-side-asn</code> - The private ASN for the Amazon side of a BGP session.</p> </li> <li> <p> <code>options.association-default-route-table-id</code> - The ID of the default association route table.</p> </li> <li> <p> <code>options.auto-accept-shared-attachments</code> - Indicates whether there is automatic acceptance of attachment requests (<code>enable</code> | <code>disable</code>).</p> </li> <li> <p> <code>options.default-route-table-association</code> - Indicates whether resource attachments are automatically associated with the default association route table (<code>enable</code> | <code>disable</code>).</p> </li> <li> <p> <code>options.default-route-table-propagation</code> - Indicates whether resource attachments automatically propagate routes to the default propagation route table (<code>enable</code> | <code>disable</code>).</p> </li> <li> <p> <code>options.dns-support</code> - Indicates whether DNS support is enabled (<code>enable</code> | <code>disable</code>).</p> </li> <li> <p> <code>options.vpn-ecmp-support</code> - Indicates whether Equal Cost Multipath Protocol support is enabled (<code>enable</code> | <code>disable</code>).</p> </li> <li> <p> <code>owner-id</code> - The ID of the Amazon Web Services account that owns the transit gateway.</p> </li> <li> <p> <code>state</code> - The state of the transit gateway (<code>available</code> | <code>deleted</code> | <code>deleting</code> | <code>modifying</code> | <code>pending</code>).</p> </li> <li> <p> <code>transit-gateway-id</code> - The ID of the transit gateway.</p> </li> <li> <p> <code>tag-key </code>- The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> </ul>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_max_results.TransitGatewayMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token for the next page of results.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeTransitGatewaysRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "transit_gateway_ids" in value:
        import aws_sdk_ec2.types.transit_gateway_id_string_list

        aws_sdk_ec2.types.transit_gateway_id_string_list.serialize_ec2_query(
            value["transit_gateway_ids"], pairs, f"{prefix}.TransitGatewayIds"
        )
    if "filters" in value:
        import aws_sdk_ec2.types.filter_list

        aws_sdk_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DescribeTransitGatewaysRequest:
    out: DescribeTransitGatewaysRequest = {}  # type: ignore[typeddict-item]
    if el.find("TransitGatewayIds") is not None:
        import aws_sdk_ec2.types.transit_gateway_id_string_list

        out["transit_gateway_ids"] = (
            aws_sdk_ec2.types.transit_gateway_id_string_list.deserialize_ec2_query(
                el, "TransitGatewayIds"
            )
        )
    if el.find("Filters") is not None:
        import aws_sdk_ec2.types.filter_list

        out["filters"] = aws_sdk_ec2.types.filter_list.deserialize_ec2_query(
            el, "Filters"
        )
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out

"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTransitGatewayConnectsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_attachment_id_string_list
    import aws_sdk_ec2.types.transit_gateway_max_results


class DescribeTransitGatewayConnectsRequest(TypedDict):
    transit_gateway_attachment_ids: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_id_string_list.TransitGatewayAttachmentIdStringList"
    ]
    """<p>The IDs of the attachments.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters. The possible values are:</p> <ul> <li> <p> <code>options.protocol</code> - The tunnel protocol (<code>gre</code>).</p> </li> <li> <p> <code>state</code> - The state of the attachment (<code>initiating</code> | <code>initiatingRequest</code> | <code>pendingAcceptance</code> | <code>rollingBack</code> | <code>pending</code> | <code>available</code> | <code>modifying</code> | <code>deleting</code> | <code>deleted</code> | <code>failed</code> | <code>rejected</code> | <code>rejecting</code> | <code>failing</code>).</p> </li> <li> <p> <code>transit-gateway-attachment-id</code> - The ID of the Connect attachment.</p> </li> <li> <p> <code>transit-gateway-id</code> - The ID of the transit gateway.</p> </li> <li> <p> <code>transport-transit-gateway-attachment-id</code> - The ID of the transit gateway attachment from which the Connect attachment was created.</p> </li> </ul>"""
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
    value: DescribeTransitGatewayConnectsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "transit_gateway_attachment_ids" in value:
        import aws_sdk_ec2.types.transit_gateway_attachment_id_string_list

        aws_sdk_ec2.types.transit_gateway_attachment_id_string_list.serialize_ec2_query(
            value["transit_gateway_attachment_ids"],
            pairs,
            f"{prefix}.TransitGatewayAttachmentIds",
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


def deserialize_ec2_query(el: Element) -> DescribeTransitGatewayConnectsRequest:
    out: DescribeTransitGatewayConnectsRequest = {}  # type: ignore[typeddict-item]
    if el.find("TransitGatewayAttachmentIds") is not None:
        import aws_sdk_ec2.types.transit_gateway_attachment_id_string_list

        out["transit_gateway_attachment_ids"] = (
            aws_sdk_ec2.types.transit_gateway_attachment_id_string_list.deserialize_ec2_query(
                el, "TransitGatewayAttachmentIds"
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

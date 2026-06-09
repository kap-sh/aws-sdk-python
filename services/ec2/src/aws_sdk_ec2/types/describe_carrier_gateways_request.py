"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCarrierGatewaysRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.carrier_gateway_id_set
    import aws_sdk_ec2.types.carrier_gateway_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.string


class DescribeCarrierGatewaysRequest(TypedDict):
    carrier_gateway_ids: NotRequired[
        "aws_sdk_ec2.types.carrier_gateway_id_set.CarrierGatewayIdSet"
    ]
    """<p>One or more carrier gateway IDs.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters.</p> <ul> <li> <p> <code>carrier-gateway-id</code> - The ID of the carrier gateway.</p> </li> <li> <p> <code>state</code> - The state of the carrier gateway (<code>pending</code> | <code>failed</code> | <code>available</code> | <code>deleting</code> | <code>deleted</code>).</p> </li> <li> <p> <code>owner-id</code> - The Amazon Web Services account ID of the owner of the carrier gateway.</p> </li> <li> <p> <code>tag</code>:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p> </li> <li> <p> <code>vpc-id</code> - The ID of the VPC associated with the carrier gateway.</p> </li> </ul>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.carrier_gateway_max_results.CarrierGatewayMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token for the next page of results.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeCarrierGatewaysRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "carrier_gateway_ids" in value:
        import aws_sdk_ec2.types.carrier_gateway_id_set

        aws_sdk_ec2.types.carrier_gateway_id_set.serialize_ec2_query(
            value["carrier_gateway_ids"], pairs, f"{prefix}.CarrierGatewayIds"
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


def deserialize_ec2_query(el: Element) -> DescribeCarrierGatewaysRequest:
    out: DescribeCarrierGatewaysRequest = {}  # type: ignore[typeddict-item]
    if el.find("CarrierGatewayIds") is not None:
        import aws_sdk_ec2.types.carrier_gateway_id_set

        out["carrier_gateway_ids"] = (
            aws_sdk_ec2.types.carrier_gateway_id_set.deserialize_ec2_query(
                el, "CarrierGatewayIds"
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

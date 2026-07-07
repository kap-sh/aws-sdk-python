"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcEndpointsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpc_endpoint_id_list


class DescribeVpcEndpointsRequest(TypedDict, closed=True):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    vpc_endpoint_ids: NotRequired[
        "aws_sdk_ec2.types.vpc_endpoint_id_list.VpcEndpointIdList"
    ]
    """<p>The IDs of the VPC endpoints.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>ip-address-type</code> - The IP address type (<code>ipv4</code> | <code>ipv6</code>).</p> </li> <li> <p> <code>service-name</code> - The name of the service.</p> </li> <li> <p> <code>service-region</code> - The Region of the service.</p> </li> <li> <p> <code>tag</code>:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p> </li> <li> <p> <code>vpc-id</code> - The ID of the VPC in which the endpoint resides.</p> </li> <li> <p> <code>vpc-endpoint-id</code> - The ID of the endpoint.</p> </li> <li> <p> <code>vpc-endpoint-state</code> - The state of the endpoint (<code>pendingAcceptance</code> | <code>pending</code> | <code>available</code> | <code>deleting</code> | <code>deleted</code> | <code>rejected</code> | <code>failed</code>).</p> </li> <li> <p> <code>vpc-endpoint-type</code> - The type of VPC endpoint (<code>Interface</code> | <code>Gateway</code> | <code>GatewayLoadBalancer</code> | <code>Resource</code> | <code>ServiceNetwork</code>).</p> </li> </ul>"""
    max_results: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum number of items to return for this request. The request returns a token that you can specify in a subsequent call to get the next set of results.</p> <p>Constraint: If the value is greater than 1,000, we return only 1,000 items.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token for the next set of items to return. (You received this token from a prior call.)</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVpcEndpointsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "vpc_endpoint_ids" in value:
        import aws_sdk_ec2.types.vpc_endpoint_id_list

        aws_sdk_ec2.types.vpc_endpoint_id_list.serialize_ec2_query(
            value["vpc_endpoint_ids"], pairs, f"{prefix}.VpcEndpointIds"
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


def deserialize_ec2_query(el: Element) -> DescribeVpcEndpointsRequest:
    out: DescribeVpcEndpointsRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("VpcEndpointIds") is not None:
        import aws_sdk_ec2.types.vpc_endpoint_id_list

        out["vpc_endpoint_ids"] = (
            aws_sdk_ec2.types.vpc_endpoint_id_list.deserialize_ec2_query(
                el, "VpcEndpointIds"
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
    return out

"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcEndpointServicesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.value_string_list


class DescribeVpcEndpointServicesRequest(TypedDict, closed=True):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    service_names: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>The service names.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>owner</code> - The ID or alias of the Amazon Web Services account that owns the service.</p> </li> <li> <p> <code>service-name</code> - The name of the service.</p> </li> <li> <p> <code>service-region</code> - The Region of the service.</p> </li> <li> <p> <code>service-type</code> - The type of service (<code>Interface</code> | <code>Gateway</code> | <code>GatewayLoadBalancer</code>).</p> </li> <li> <p> <code>supported-ip-address-types</code> - The IP address type (<code>ipv4</code> | <code>ipv6</code>).</p> </li> <li> <p> <code>tag</code>:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p> </li> </ul>"""
    max_results: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum number of items to return for this request. The request returns a token that you can specify in a subsequent call to get the next set of results.</p> <p>Constraint: If the value is greater than 1,000, we return only 1,000 items.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token for the next set of items to return. (You received this token from a prior call.)</p>"""
    service_regions: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>The service Regions.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVpcEndpointServicesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "service_names" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["service_names"], pairs, f"{prefix}.ServiceNames"
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
    if "service_regions" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["service_regions"], pairs, f"{prefix}.ServiceRegions"
        )


def deserialize_ec2_query(el: Element) -> DescribeVpcEndpointServicesRequest:
    out: DescribeVpcEndpointServicesRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("ServiceNames") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["service_names"] = (
            aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
                el, "ServiceNames"
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
    if el.find("ServiceRegions") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["service_regions"] = (
            aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
                el, "ServiceRegions"
            )
        )
    return out

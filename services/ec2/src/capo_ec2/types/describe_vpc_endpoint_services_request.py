"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcEndpointServicesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.filter_list
    import capo_ec2.types.integer
    import capo_ec2.types.string
    import capo_ec2.types.value_string_list


class DescribeVpcEndpointServicesRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    service_names: NotRequired["capo_ec2.types.value_string_list.ValueStringList"]
    """<p>The service names.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>owner</code> - The ID or alias of the Amazon Web Services account that owns the service.</p> </li> <li> <p> <code>service-name</code> - The name of the service.</p> </li> <li> <p> <code>service-region</code> - The Region of the service.</p> </li> <li> <p> <code>service-type</code> - The type of service (<code>Interface</code> | <code>Gateway</code> | <code>GatewayLoadBalancer</code>).</p> </li> <li> <p> <code>supported-ip-address-types</code> - The IP address type (<code>ipv4</code> | <code>ipv6</code>).</p> </li> <li> <p> <code>tag</code>:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p> </li> </ul>"""
    max_results: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The maximum number of items to return for this request. The request returns a token that you can specify in a subsequent call to get the next set of results.</p> <p>Constraint: If the value is greater than 1,000, we return only 1,000 items.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token for the next set of items to return. (You received this token from a prior call.)</p>"""
    service_regions: NotRequired["capo_ec2.types.value_string_list.ValueStringList"]
    """<p>The service Regions.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVpcEndpointServicesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "service_names" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["service_names"], pairs, f"{key_prefix}ServiceName"
        )
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "service_regions" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["service_regions"], pairs, f"{key_prefix}ServiceRegion"
        )


def deserialize_ec2_query(el: Element) -> DescribeVpcEndpointServicesRequest:
    out: DescribeVpcEndpointServicesRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("ServiceName") is not None:
        import capo_ec2.types.value_string_list

        out["service_names"] = capo_ec2.types.value_string_list.deserialize_ec2_query(
            el, "ServiceName"
        )
    if el.find("Filter") is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(el, "Filter")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("ServiceRegion") is not None:
        import capo_ec2.types.value_string_list

        out["service_regions"] = capo_ec2.types.value_string_list.deserialize_ec2_query(
            el, "ServiceRegion"
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeServiceLinkVirtualInterfacesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.service_link_max_results
    import aws_sdk_ec2.types.service_link_virtual_interface_id_set
    import aws_sdk_ec2.types.string


class DescribeServiceLinkVirtualInterfacesRequest(TypedDict):
    service_link_virtual_interface_ids: NotRequired[
        "aws_sdk_ec2.types.service_link_virtual_interface_id_set.ServiceLinkVirtualInterfaceIdSet"
    ]
    """<p>The IDs of the service link virtual interfaces.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters to use for narrowing down the request. The following filters are supported:</p> <ul> <li> <p> <code>outpost-lag-id</code> - The ID of the Outpost LAG.</p> </li> <li> <p> <code>outpost-arn</code> - The Outpost ARN.</p> </li> <li> <p> <code>owner-id</code> - The ID of the Amazon Web Services account that owns the service link virtual interface.</p> </li> <li> <p> <code>state</code> - The state of the Outpost LAG.</p> </li> <li> <p> <code>vlan</code> - The ID of the address pool.</p> </li> <li> <p> <code>service-link-virtual-interface-id</code> - The ID of the service link virtual interface.</p> </li> <li> <p> <code>local-gateway-virtual-interface-id</code> - The ID of the local gateway virtual interface.</p> </li> </ul>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.service_link_max_results.ServiceLinkMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token for the next page of results.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeServiceLinkVirtualInterfacesRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "service_link_virtual_interface_ids" in value:
        import aws_sdk_ec2.types.service_link_virtual_interface_id_set

        aws_sdk_ec2.types.service_link_virtual_interface_id_set.serialize_ec2_query(
            value["service_link_virtual_interface_ids"],
            pairs,
            f"{prefix}.ServiceLinkVirtualInterfaceIds",
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


def deserialize_ec2_query(el: Element) -> DescribeServiceLinkVirtualInterfacesRequest:
    out: DescribeServiceLinkVirtualInterfacesRequest = {}  # type: ignore[typeddict-item]
    if el.find("ServiceLinkVirtualInterfaceIds") is not None:
        import aws_sdk_ec2.types.service_link_virtual_interface_id_set

        out["service_link_virtual_interface_ids"] = (
            aws_sdk_ec2.types.service_link_virtual_interface_id_set.deserialize_ec2_query(
                el, "ServiceLinkVirtualInterfaceIds"
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

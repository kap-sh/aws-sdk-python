"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamDiscoveredRoutesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.filter_list
    import capo_ec2.types.ipam_max_results
    import capo_ec2.types.ipam_resource_discovery_id
    import capo_ec2.types.next_token
    import capo_ec2.types.string


class GetIpamDiscoveredRoutesRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_resource_discovery_id: NotRequired[
        "capo_ec2.types.ipam_resource_discovery_id.IpamResourceDiscoveryId"
    ]
    """<p>The ID of the IPAM resource discovery.</p>"""
    resource_region: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Web Services Region to retrieve discovered routes for.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>One or more filters to apply to the results.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""
    max_results: NotRequired["capo_ec2.types.ipam_max_results.IpamMaxResults"]
    """<p>The maximum number of results to return in a single call. If not specified, all available results are returned. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetIpamDiscoveredRoutesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "ipam_resource_discovery_id" in value:
        pairs.append(
            (
                f"{key_prefix}IpamResourceDiscoveryId",
                str(value["ipam_resource_discovery_id"]),
            )
        )
    if "resource_region" in value:
        pairs.append((f"{key_prefix}ResourceRegion", str(value["resource_region"])))
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))


def deserialize_ec2_query(el: Element) -> GetIpamDiscoveredRoutesRequest:
    out: GetIpamDiscoveredRoutesRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_ipam_resource_discovery_id = el.find("IpamResourceDiscoveryId")
    if child_ipam_resource_discovery_id is not None:
        out["ipam_resource_discovery_id"] = str(
            child_ipam_resource_discovery_id.text or ""
        )
    child_resource_region = el.find("ResourceRegion")
    if child_resource_region is not None:
        out["resource_region"] = str(child_resource_region.text or "")
    child_filters = el.find("Filter")
    if child_filters is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(child_filters)
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    return out

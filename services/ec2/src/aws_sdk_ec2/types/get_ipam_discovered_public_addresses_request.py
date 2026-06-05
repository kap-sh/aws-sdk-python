"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamDiscoveredPublicAddressesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.ipam_max_results
    import aws_sdk_ec2.types.ipam_resource_discovery_id
    import aws_sdk_ec2.types.next_token
    import aws_sdk_ec2.types.string


class GetIpamDiscoveredPublicAddressesRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_resource_discovery_id: NotRequired[
        "aws_sdk_ec2.types.ipam_resource_discovery_id.IpamResourceDiscoveryId"
    ]
    """<p>An IPAM resource discovery ID.</p>"""
    address_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services Region for the IP address.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>Filters.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""
    max_results: NotRequired["aws_sdk_ec2.types.ipam_max_results.IpamMaxResults"]
    """<p>The maximum number of IPAM discovered public addresses to return in one page of results.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetIpamDiscoveredPublicAddressesRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "ipam_resource_discovery_id" in value:
        pairs.append(
            (
                f"{prefix}.IpamResourceDiscoveryId",
                str(value["ipam_resource_discovery_id"]),
            )
        )
    if "address_region" in value:
        pairs.append((f"{prefix}.AddressRegion", str(value["address_region"])))
    if "filters" in value:
        import aws_sdk_ec2.types.filter_list

        aws_sdk_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))


def deserialize_ec2_query(el: Element) -> GetIpamDiscoveredPublicAddressesRequest:
    out: GetIpamDiscoveredPublicAddressesRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_ipam_resource_discovery_id = el.find("IpamResourceDiscoveryId")
    if child_ipam_resource_discovery_id is not None:
        out["ipam_resource_discovery_id"] = str(
            child_ipam_resource_discovery_id.text or ""
        )
    child_address_region = el.find("AddressRegion")
    if child_address_region is not None:
        out["address_region"] = str(child_address_region.text or "")
    if el.find("Filters") is not None:
        import aws_sdk_ec2.types.filter_list

        out["filters"] = aws_sdk_ec2.types.filter_list.deserialize_ec2_query(
            el, "Filters"
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    return out

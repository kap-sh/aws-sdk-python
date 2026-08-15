"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamInternetRegistryAssociationAsnsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.filter_list
    import capo_ec2.types.ipam_internet_registry_association_id
    import capo_ec2.types.ipam_max_results
    import capo_ec2.types.next_token


class GetIpamInternetRegistryAssociationAsnsRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_internet_registry_association_id: NotRequired[
        "capo_ec2.types.ipam_internet_registry_association_id.IpamInternetRegistryAssociationId"
    ]
    """<p>The ID of the IPAM internet registry association.</p>"""
    max_results: NotRequired["capo_ec2.types.ipam_max_results.IpamMaxResults"]
    """<p>The maximum number of results to return in a single call. If not specified, all available results are returned. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>One or more filters to apply to the results.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetIpamInternetRegistryAssociationAsnsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "ipam_internet_registry_association_id" in value:
        pairs.append(
            (
                f"{key_prefix}IpamInternetRegistryAssociationId",
                str(value["ipam_internet_registry_association_id"]),
            )
        )
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )


def deserialize_ec2_query(el: Element) -> GetIpamInternetRegistryAssociationAsnsRequest:
    out: GetIpamInternetRegistryAssociationAsnsRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_ipam_internet_registry_association_id = el.find(
        "IpamInternetRegistryAssociationId"
    )
    if child_ipam_internet_registry_association_id is not None:
        out["ipam_internet_registry_association_id"] = str(
            child_ipam_internet_registry_association_id.text or ""
        )
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_filters = el.find("Filter")
    if child_filters is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(child_filters)
    return out

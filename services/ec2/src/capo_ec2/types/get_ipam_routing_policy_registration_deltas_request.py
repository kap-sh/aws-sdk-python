"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamRoutingPolicyRegistrationDeltasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.chronological_order
    import capo_ec2.types.ipam_internet_registry_association_id
    import capo_ec2.types.ipam_max_results
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.next_token
    import capo_ec2.types.string


class GetIpamRoutingPolicyRegistrationDeltasRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_internet_registry_association_id: NotRequired[
        "capo_ec2.types.ipam_internet_registry_association_id.IpamInternetRegistryAssociationId"
    ]
    """<p>The ID of the IPAM internet registry association.</p>"""
    delta_id: NotRequired["capo_ec2.types.string.String"]
    """<p>Filter results to a specific delta ID.</p>"""
    start_time: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The start of the time range to filter deltas by.</p>"""
    end_time: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The end of the time range to filter deltas by.</p>"""
    chronological_order: NotRequired[
        "capo_ec2.types.chronological_order.ChronologicalOrder"
    ]
    """<p>The chronological order to return results in. Valid values: <code>forward</code> | <code>reverse</code>.</p>"""
    max_results: NotRequired["capo_ec2.types.ipam_max_results.IpamMaxResults"]
    """<p>The maximum number of results to return in a single call. If not specified, all available results are returned. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetIpamRoutingPolicyRegistrationDeltasRequest,
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
    if "delta_id" in value:
        pairs.append((f"{key_prefix}DeltaId", str(value["delta_id"])))
    if "start_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["start_time"], pairs, f"{key_prefix}StartTime"
        )
    if "end_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["end_time"], pairs, f"{key_prefix}EndTime"
        )
    if "chronological_order" in value:
        import capo_ec2.types.chronological_order

        capo_ec2.types.chronological_order.serialize_ec2_query(
            value["chronological_order"], pairs, f"{key_prefix}ChronologicalOrder"
        )
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetIpamRoutingPolicyRegistrationDeltasRequest:
    out: GetIpamRoutingPolicyRegistrationDeltasRequest = {}  # type: ignore[typeddict-item]
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
    child_delta_id = el.find("DeltaId")
    if child_delta_id is not None:
        out["delta_id"] = str(child_delta_id.text or "")
    child_start_time = el.find("StartTime")
    if child_start_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["start_time"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_start_time
        )
    child_end_time = el.find("EndTime")
    if child_end_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["end_time"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_end_time
        )
    child_chronological_order = el.find("ChronologicalOrder")
    if child_chronological_order is not None:
        import capo_ec2.types.chronological_order

        out["chronological_order"] = (
            capo_ec2.types.chronological_order.deserialize_ec2_query(
                child_chronological_order
            )
        )
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out

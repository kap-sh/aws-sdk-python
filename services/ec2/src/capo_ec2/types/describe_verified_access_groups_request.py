"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVerifiedAccessGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.describe_verified_access_group_max_results
    import capo_ec2.types.filter_list
    import capo_ec2.types.next_token
    import capo_ec2.types.verified_access_group_id_list
    import capo_ec2.types.verified_access_instance_id


class DescribeVerifiedAccessGroupsRequest(TypedDict, closed=True):
    verified_access_group_ids: NotRequired[
        "capo_ec2.types.verified_access_group_id_list.VerifiedAccessGroupIdList"
    ]
    """<p>The ID of the Verified Access groups.</p>"""
    verified_access_instance_id: NotRequired[
        "capo_ec2.types.verified_access_instance_id.VerifiedAccessInstanceId"
    ]
    """<p>The ID of the Verified Access instance.</p>"""
    max_results: NotRequired[
        "capo_ec2.types.describe_verified_access_group_max_results.DescribeVerifiedAccessGroupMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>One or more filters. Filter names and values are case-sensitive.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVerifiedAccessGroupsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "verified_access_group_ids" in value:
        import capo_ec2.types.verified_access_group_id_list

        capo_ec2.types.verified_access_group_id_list.serialize_ec2_query(
            value["verified_access_group_ids"],
            pairs,
            f"{key_prefix}VerifiedAccessGroupId",
        )
    if "verified_access_instance_id" in value:
        pairs.append(
            (
                f"{key_prefix}VerifiedAccessInstanceId",
                str(value["verified_access_instance_id"]),
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
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DescribeVerifiedAccessGroupsRequest:
    out: DescribeVerifiedAccessGroupsRequest = {}  # type: ignore[typeddict-item]
    if el.find("VerifiedAccessGroupId") is not None:
        import capo_ec2.types.verified_access_group_id_list

        out["verified_access_group_ids"] = (
            capo_ec2.types.verified_access_group_id_list.deserialize_ec2_query(
                el, "VerifiedAccessGroupId"
            )
        )
    child_verified_access_instance_id = el.find("VerifiedAccessInstanceId")
    if child_verified_access_instance_id is not None:
        out["verified_access_instance_id"] = str(
            child_verified_access_instance_id.text or ""
        )
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("Filter") is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(el, "Filter")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out

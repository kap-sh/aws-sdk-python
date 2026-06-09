"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSnapshotsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.owner_string_list
    import aws_sdk_ec2.types.restorable_by_string_list
    import aws_sdk_ec2.types.snapshot_id_string_list
    import aws_sdk_ec2.types.string


class DescribeSnapshotsRequest(TypedDict):
    max_results: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    owner_ids: NotRequired["aws_sdk_ec2.types.owner_string_list.OwnerStringList"]
    """<p>Scopes the results to snapshots with the specified owners. You can specify a combination of Amazon Web Services account IDs, <code>self</code>, and <code>amazon</code>.</p>"""
    restorable_by_user_ids: NotRequired[
        "aws_sdk_ec2.types.restorable_by_string_list.RestorableByStringList"
    ]
    """<p>The IDs of the Amazon Web Services accounts that can create volumes from the snapshot.</p>"""
    snapshot_ids: NotRequired[
        "aws_sdk_ec2.types.snapshot_id_string_list.SnapshotIdStringList"
    ]
    """<p>The snapshot IDs.</p> <p>Default: Describes the snapshots for which you have create volume permissions.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>description</code> - A description of the snapshot.</p> </li> <li> <p> <code>encrypted</code> - Indicates whether the snapshot is encrypted (<code>true</code> | <code>false</code>)</p> </li> <li> <p> <code>owner-alias</code> - The owner alias, from an Amazon-maintained list (<code>amazon</code>). This is not the user-configured Amazon Web Services account alias set using the IAM console. We recommend that you use the related parameter instead of this filter.</p> </li> <li> <p> <code>owner-id</code> - The Amazon Web Services account ID of the owner. We recommend that you use the related parameter instead of this filter.</p> </li> <li> <p> <code>progress</code> - The progress of the snapshot, as a percentage (for example, 80%).</p> </li> <li> <p> <code>snapshot-id</code> - The snapshot ID.</p> </li> <li> <p> <code>start-time</code> - The time stamp when the snapshot was initiated.</p> </li> <li> <p> <code>status</code> - The status of the snapshot (<code>pending</code> | <code>completed</code> | <code>error</code>).</p> </li> <li> <p> <code>storage-tier</code> - The storage tier of the snapshot (<code>archive</code> | <code>standard</code>).</p> </li> <li> <p> <code>transfer-type</code> - The type of operation used to create the snapshot (<code>time-based</code> | <code>standard</code>).</p> </li> <li> <p> <code>tag</code>:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p> </li> <li> <p> <code>volume-id</code> - The ID of the volume the snapshot is for.</p> </li> <li> <p> <code>volume-size</code> - The size of the volume, in GiB.</p> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeSnapshotsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "owner_ids" in value:
        import aws_sdk_ec2.types.owner_string_list

        aws_sdk_ec2.types.owner_string_list.serialize_ec2_query(
            value["owner_ids"], pairs, f"{prefix}.OwnerIds"
        )
    if "restorable_by_user_ids" in value:
        import aws_sdk_ec2.types.restorable_by_string_list

        aws_sdk_ec2.types.restorable_by_string_list.serialize_ec2_query(
            value["restorable_by_user_ids"], pairs, f"{prefix}.RestorableByUserIds"
        )
    if "snapshot_ids" in value:
        import aws_sdk_ec2.types.snapshot_id_string_list

        aws_sdk_ec2.types.snapshot_id_string_list.serialize_ec2_query(
            value["snapshot_ids"], pairs, f"{prefix}.SnapshotIds"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "filters" in value:
        import aws_sdk_ec2.types.filter_list

        aws_sdk_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )


def deserialize_ec2_query(el: Element) -> DescribeSnapshotsRequest:
    out: DescribeSnapshotsRequest = {}  # type: ignore[typeddict-item]
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("OwnerIds") is not None:
        import aws_sdk_ec2.types.owner_string_list

        out["owner_ids"] = aws_sdk_ec2.types.owner_string_list.deserialize_ec2_query(
            el, "OwnerIds"
        )
    if el.find("RestorableByUserIds") is not None:
        import aws_sdk_ec2.types.restorable_by_string_list

        out["restorable_by_user_ids"] = (
            aws_sdk_ec2.types.restorable_by_string_list.deserialize_ec2_query(
                el, "RestorableByUserIds"
            )
        )
    if el.find("SnapshotIds") is not None:
        import aws_sdk_ec2.types.snapshot_id_string_list

        out["snapshot_ids"] = (
            aws_sdk_ec2.types.snapshot_id_string_list.deserialize_ec2_query(
                el, "SnapshotIds"
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("Filters") is not None:
        import aws_sdk_ec2.types.filter_list

        out["filters"] = aws_sdk_ec2.types.filter_list.deserialize_ec2_query(
            el, "Filters"
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.fsx#DescribeSnapshotsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.include_shared
    import capo_fsx.types.max_results
    import capo_fsx.types.next_token
    import capo_fsx.types.snapshot_filters
    import capo_fsx.types.snapshot_ids


class DescribeSnapshotsRequest(TypedDict, closed=True):
    snapshot_ids: NotRequired["capo_fsx.types.snapshot_ids.SnapshotIds"]
    """<p>The IDs of the snapshots that you want to retrieve. This parameter value overrides any filters. If any IDs aren't found, a <code>SnapshotNotFound</code> error occurs.</p>"""
    filters: NotRequired["capo_fsx.types.snapshot_filters.SnapshotFilters"]
    """<p>The filters structure. The supported names are <code>file-system-id</code> or <code>volume-id</code>.</p>"""
    max_results: NotRequired["capo_fsx.types.max_results.MaxResults"]
    next_token: NotRequired["capo_fsx.types.next_token.NextToken"]
    include_shared: NotRequired["capo_fsx.types.include_shared.IncludeShared"]
    """<p>Set to <code>false</code> (default) if you want to only see the snapshots owned by your Amazon Web Services account. Set to <code>true</code> if you want to see the snapshots in your account and the ones shared with you from another account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSnapshotsRequest) -> dict:
    out: dict = {}
    if "snapshot_ids" in value:
        import capo_fsx.types.snapshot_ids

        out["SnapshotIds"] = capo_fsx.types.snapshot_ids.serialize_aws_json_1_1(
            value["snapshot_ids"]
        )
    if "filters" in value:
        import capo_fsx.types.snapshot_filters

        out["Filters"] = capo_fsx.types.snapshot_filters.serialize_aws_json_1_1(
            value["filters"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "include_shared" in value:
        out["IncludeShared"] = value["include_shared"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSnapshotsRequest:
    out: DescribeSnapshotsRequest = {}  # type: ignore[typeddict-item]
    if "SnapshotIds" in data:
        import capo_fsx.types.snapshot_ids

        out["snapshot_ids"] = capo_fsx.types.snapshot_ids.deserialize_aws_json_1_1(
            data["SnapshotIds"]
        )
    if "Filters" in data:
        import capo_fsx.types.snapshot_filters

        out["filters"] = capo_fsx.types.snapshot_filters.deserialize_aws_json_1_1(
            data["Filters"]
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "IncludeShared" in data:
        out["include_shared"] = data["IncludeShared"]
    return out

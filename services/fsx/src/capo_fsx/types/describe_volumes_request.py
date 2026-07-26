"""Generated from Smithy shape ``com.amazonaws.fsx#DescribeVolumesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.max_results
    import capo_fsx.types.next_token
    import capo_fsx.types.volume_filters
    import capo_fsx.types.volume_ids


class DescribeVolumesRequest(TypedDict, closed=True):
    volume_ids: NotRequired["capo_fsx.types.volume_ids.VolumeIds"]
    """<p>The IDs of the volumes whose descriptions you want to retrieve.</p>"""
    filters: NotRequired["capo_fsx.types.volume_filters.VolumeFilters"]
    """<p>Enter a filter <code>Name</code> and <code>Values</code> pair to view a select set of volumes.</p>"""
    max_results: NotRequired["capo_fsx.types.max_results.MaxResults"]
    next_token: NotRequired["capo_fsx.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeVolumesRequest) -> dict:
    out: dict = {}
    if "volume_ids" in value:
        import capo_fsx.types.volume_ids

        out["VolumeIds"] = capo_fsx.types.volume_ids.serialize_aws_json_1_1(
            value["volume_ids"]
        )
    if "filters" in value:
        import capo_fsx.types.volume_filters

        out["Filters"] = capo_fsx.types.volume_filters.serialize_aws_json_1_1(
            value["filters"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeVolumesRequest:
    out: DescribeVolumesRequest = {}  # type: ignore[typeddict-item]
    if "VolumeIds" in data:
        import capo_fsx.types.volume_ids

        out["volume_ids"] = capo_fsx.types.volume_ids.deserialize_aws_json_1_1(
            data["VolumeIds"]
        )
    if "Filters" in data:
        import capo_fsx.types.volume_filters

        out["filters"] = capo_fsx.types.volume_filters.deserialize_aws_json_1_1(
            data["Filters"]
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

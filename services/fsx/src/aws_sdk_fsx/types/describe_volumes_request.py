"""Generated from Smithy shape ``com.amazonaws.fsx#DescribeVolumesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.max_results
    import aws_sdk_fsx.types.next_token
    import aws_sdk_fsx.types.volume_filters
    import aws_sdk_fsx.types.volume_ids


class DescribeVolumesRequest(TypedDict):
    volume_ids: NotRequired["aws_sdk_fsx.types.volume_ids.VolumeIds"]
    """<p>The IDs of the volumes whose descriptions you want to retrieve.</p>"""
    filters: NotRequired["aws_sdk_fsx.types.volume_filters.VolumeFilters"]
    """<p>Enter a filter <code>Name</code> and <code>Values</code> pair to view a select set of volumes.</p>"""
    max_results: NotRequired["aws_sdk_fsx.types.max_results.MaxResults"]
    next_token: NotRequired["aws_sdk_fsx.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeVolumesRequest) -> dict:
    out: dict = {}
    if "volume_ids" in value:
        import aws_sdk_fsx.types.volume_ids

        out["VolumeIds"] = aws_sdk_fsx.types.volume_ids.serialize_aws_json_1_1(
            value["volume_ids"]
        )
    if "filters" in value:
        import aws_sdk_fsx.types.volume_filters

        out["Filters"] = aws_sdk_fsx.types.volume_filters.serialize_aws_json_1_1(
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
        import aws_sdk_fsx.types.volume_ids

        out["volume_ids"] = aws_sdk_fsx.types.volume_ids.deserialize_aws_json_1_1(
            data["VolumeIds"]
        )
    if "Filters" in data:
        import aws_sdk_fsx.types.volume_filters

        out["filters"] = aws_sdk_fsx.types.volume_filters.deserialize_aws_json_1_1(
            data["Filters"]
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

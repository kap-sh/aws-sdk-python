"""Generated from Smithy shape ``com.amazonaws.fsx#SnapshotFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.snapshot_filter_name
    import aws_sdk_fsx.types.snapshot_filter_values


class SnapshotFilter(TypedDict):
    name: NotRequired["aws_sdk_fsx.types.snapshot_filter_name.SnapshotFilterName"]
    """<p>The name of the filter to use. You can filter by the <code>file-system-id</code> or by <code>volume-id</code>.</p>"""
    values: NotRequired["aws_sdk_fsx.types.snapshot_filter_values.SnapshotFilterValues"]
    """<p>The <code>file-system-id</code> or <code>volume-id</code> that you are filtering for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotFilter) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_fsx.types.snapshot_filter_name

        out["Name"] = aws_sdk_fsx.types.snapshot_filter_name.serialize_aws_json_1_1(
            value["name"]
        )
    if "values" in value:
        import aws_sdk_fsx.types.snapshot_filter_values

        out["Values"] = aws_sdk_fsx.types.snapshot_filter_values.serialize_aws_json_1_1(
            value["values"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SnapshotFilter:
    out: SnapshotFilter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import aws_sdk_fsx.types.snapshot_filter_name

        out["name"] = aws_sdk_fsx.types.snapshot_filter_name.deserialize_aws_json_1_1(
            data["Name"]
        )
    if "Values" in data:
        import aws_sdk_fsx.types.snapshot_filter_values

        out["values"] = (
            aws_sdk_fsx.types.snapshot_filter_values.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    return out

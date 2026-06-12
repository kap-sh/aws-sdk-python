"""Generated from Smithy shape ``com.amazonaws.fsx#DescribeSnapshotsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.next_token
    import aws_sdk_fsx.types.snapshots


class DescribeSnapshotsResponse(TypedDict):
    snapshots: NotRequired["aws_sdk_fsx.types.snapshots.Snapshots"]
    """<p>An array of snapshots.</p>"""
    next_token: NotRequired["aws_sdk_fsx.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSnapshotsResponse) -> dict:
    out: dict = {}
    if "snapshots" in value:
        import aws_sdk_fsx.types.snapshots

        out["Snapshots"] = aws_sdk_fsx.types.snapshots.serialize_aws_json_1_1(
            value["snapshots"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSnapshotsResponse:
    out: DescribeSnapshotsResponse = {}  # type: ignore[typeddict-item]
    if "Snapshots" in data:
        import aws_sdk_fsx.types.snapshots

        out["snapshots"] = aws_sdk_fsx.types.snapshots.deserialize_aws_json_1_1(
            data["Snapshots"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ListSnapshotsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.snapshot_list


class ListSnapshotsResponse(TypedDict):
    next_token: NotRequired["str"]
    """<p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>"""
    snapshots: NotRequired[
        "aws_sdk_redshift_serverless.types.snapshot_list.SnapshotList"
    ]
    """<p>All of the returned snapshot objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSnapshotsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "snapshots" in value:
        import aws_sdk_redshift_serverless.types.snapshot_list

        out["snapshots"] = (
            aws_sdk_redshift_serverless.types.snapshot_list.serialize_aws_json_1_1(
                value["snapshots"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSnapshotsResponse:
    out: ListSnapshotsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "snapshots" in data:
        import aws_sdk_redshift_serverless.types.snapshot_list

        out["snapshots"] = (
            aws_sdk_redshift_serverless.types.snapshot_list.deserialize_aws_json_1_1(
                data["snapshots"]
            )
        )
    return out

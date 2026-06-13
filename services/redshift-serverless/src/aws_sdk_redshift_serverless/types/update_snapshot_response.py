"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#UpdateSnapshotResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.snapshot


class UpdateSnapshotResponse(TypedDict):
    snapshot: NotRequired["aws_sdk_redshift_serverless.types.snapshot.Snapshot"]
    """<p>The updated snapshot object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSnapshotResponse) -> dict:
    out: dict = {}
    if "snapshot" in value:
        import aws_sdk_redshift_serverless.types.snapshot

        out["snapshot"] = (
            aws_sdk_redshift_serverless.types.snapshot.serialize_aws_json_1_1(
                value["snapshot"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSnapshotResponse:
    out: UpdateSnapshotResponse = {}  # type: ignore[typeddict-item]
    if "snapshot" in data:
        import aws_sdk_redshift_serverless.types.snapshot

        out["snapshot"] = (
            aws_sdk_redshift_serverless.types.snapshot.deserialize_aws_json_1_1(
                data["snapshot"]
            )
        )
    return out

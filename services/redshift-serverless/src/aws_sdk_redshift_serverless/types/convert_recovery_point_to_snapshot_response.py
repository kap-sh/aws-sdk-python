"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ConvertRecoveryPointToSnapshotResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.snapshot


class ConvertRecoveryPointToSnapshotResponse(TypedDict, closed=True):
    snapshot: NotRequired["aws_sdk_redshift_serverless.types.snapshot.Snapshot"]
    """<p>The snapshot converted from the recovery point.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConvertRecoveryPointToSnapshotResponse) -> dict:
    out: dict = {}
    if "snapshot" in value:
        import aws_sdk_redshift_serverless.types.snapshot

        out["snapshot"] = (
            aws_sdk_redshift_serverless.types.snapshot.serialize_aws_json_1_1(
                value["snapshot"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConvertRecoveryPointToSnapshotResponse:
    out: ConvertRecoveryPointToSnapshotResponse = {}  # type: ignore[typeddict-item]
    if "snapshot" in data:
        import aws_sdk_redshift_serverless.types.snapshot

        out["snapshot"] = (
            aws_sdk_redshift_serverless.types.snapshot.deserialize_aws_json_1_1(
                data["snapshot"]
            )
        )
    return out

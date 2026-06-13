"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#RestoreFromSnapshotResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.namespace


class RestoreFromSnapshotResponse(TypedDict):
    snapshot_name: NotRequired["str"]
    """<p>The name of the snapshot used to restore the namespace.</p>"""
    owner_account: NotRequired["str"]
    """<p>The owner Amazon Web Services; account of the snapshot that was restored.</p>"""
    namespace: NotRequired["aws_sdk_redshift_serverless.types.namespace.Namespace"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RestoreFromSnapshotResponse) -> dict:
    out: dict = {}
    if "snapshot_name" in value:
        out["snapshotName"] = value["snapshot_name"]
    if "owner_account" in value:
        out["ownerAccount"] = value["owner_account"]
    if "namespace" in value:
        import aws_sdk_redshift_serverless.types.namespace

        out["namespace"] = (
            aws_sdk_redshift_serverless.types.namespace.serialize_aws_json_1_1(
                value["namespace"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RestoreFromSnapshotResponse:
    out: RestoreFromSnapshotResponse = {}  # type: ignore[typeddict-item]
    if "snapshotName" in data:
        out["snapshot_name"] = data["snapshotName"]
    if "ownerAccount" in data:
        out["owner_account"] = data["ownerAccount"]
    if "namespace" in data:
        import aws_sdk_redshift_serverless.types.namespace

        out["namespace"] = (
            aws_sdk_redshift_serverless.types.namespace.deserialize_aws_json_1_1(
                data["namespace"]
            )
        )
    return out

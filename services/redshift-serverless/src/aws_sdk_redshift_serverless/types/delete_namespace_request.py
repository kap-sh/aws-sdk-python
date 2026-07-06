"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#DeleteNamespaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.namespace_name


class DeleteNamespaceRequest(TypedDict, closed=True):
    namespace_name: "aws_sdk_redshift_serverless.types.namespace_name.NamespaceName"
    """<p>The name of the namespace to delete.</p>"""
    final_snapshot_name: NotRequired["str"]
    """<p>The name of the snapshot to be created before the namespace is deleted.</p>"""
    final_snapshot_retention_period: NotRequired["int"]
    """<p>How long to retain the final snapshot.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteNamespaceRequest) -> dict:
    out: dict = {}
    out["namespaceName"] = value["namespace_name"]
    if "final_snapshot_name" in value:
        out["finalSnapshotName"] = value["final_snapshot_name"]
    if "final_snapshot_retention_period" in value:
        out["finalSnapshotRetentionPeriod"] = value["final_snapshot_retention_period"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteNamespaceRequest:
    out: DeleteNamespaceRequest = {}  # type: ignore[typeddict-item]
    if "namespaceName" in data:
        out["namespace_name"] = data["namespaceName"]
    else:
        raise DeserializationError("DeleteNamespaceRequest.namespace_name required")
    if "finalSnapshotName" in data:
        out["final_snapshot_name"] = data["finalSnapshotName"]
    if "finalSnapshotRetentionPeriod" in data:
        out["final_snapshot_retention_period"] = data["finalSnapshotRetentionPeriod"]
    return out

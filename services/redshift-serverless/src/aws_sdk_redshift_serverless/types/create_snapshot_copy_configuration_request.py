"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#CreateSnapshotCopyConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.kms_key_id
    import aws_sdk_redshift_serverless.types.namespace_name


class CreateSnapshotCopyConfigurationRequest(TypedDict, closed=True):
    namespace_name: "aws_sdk_redshift_serverless.types.namespace_name.NamespaceName"
    """<p>The name of the namespace to copy snapshots from.</p>"""
    destination_region: "str"
    """<p>The destination Amazon Web Services Region that you want to copy snapshots to.</p>"""
    snapshot_retention_period: NotRequired["int"]
    """<p>The retention period of the snapshots that you copy to the destination Amazon Web Services Region.</p>"""
    destination_kms_key_id: NotRequired[
        "aws_sdk_redshift_serverless.types.kms_key_id.KmsKeyId"
    ]
    """<p>The KMS key to use to encrypt your snapshots in the destination Amazon Web Services Region.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSnapshotCopyConfigurationRequest) -> dict:
    out: dict = {}
    out["namespaceName"] = value["namespace_name"]
    out["destinationRegion"] = value["destination_region"]
    if "snapshot_retention_period" in value:
        out["snapshotRetentionPeriod"] = value["snapshot_retention_period"]
    if "destination_kms_key_id" in value:
        out["destinationKmsKeyId"] = value["destination_kms_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSnapshotCopyConfigurationRequest:
    out: CreateSnapshotCopyConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "namespaceName" in data:
        out["namespace_name"] = data["namespaceName"]
    else:
        raise DeserializationError(
            "CreateSnapshotCopyConfigurationRequest.namespace_name required"
        )
    if "destinationRegion" in data:
        out["destination_region"] = data["destinationRegion"]
    else:
        raise DeserializationError(
            "CreateSnapshotCopyConfigurationRequest.destination_region required"
        )
    if "snapshotRetentionPeriod" in data:
        out["snapshot_retention_period"] = data["snapshotRetentionPeriod"]
    if "destinationKmsKeyId" in data:
        out["destination_kms_key_id"] = data["destinationKmsKeyId"]
    return out

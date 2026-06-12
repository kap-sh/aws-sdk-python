"""Generated from Smithy shape ``com.amazonaws.memorydb#CreateSnapshotRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_memorydb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.string
    import aws_sdk_memorydb.types.tag_list


class CreateSnapshotRequest(TypedDict):
    cluster_name: "aws_sdk_memorydb.types.string.String"
    """<p>The snapshot is created from this cluster.</p>"""
    snapshot_name: "aws_sdk_memorydb.types.string.String"
    """<p>A name for the snapshot being created.</p>"""
    kms_key_id: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The ID of the KMS key used to encrypt the snapshot.</p>"""
    tags: NotRequired["aws_sdk_memorydb.types.tag_list.TagList"]
    """<p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSnapshotRequest) -> dict:
    out: dict = {}
    out["ClusterName"] = value["cluster_name"]
    out["SnapshotName"] = value["snapshot_name"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "tags" in value:
        import aws_sdk_memorydb.types.tag_list

        out["Tags"] = aws_sdk_memorydb.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSnapshotRequest:
    out: CreateSnapshotRequest = {}  # type: ignore[typeddict-item]
    if "ClusterName" in data:
        out["cluster_name"] = data["ClusterName"]
    else:
        raise DeserializationError("CreateSnapshotRequest.cluster_name required")
    if "SnapshotName" in data:
        out["snapshot_name"] = data["SnapshotName"]
    else:
        raise DeserializationError("CreateSnapshotRequest.snapshot_name required")
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "Tags" in data:
        import aws_sdk_memorydb.types.tag_list

        out["tags"] = aws_sdk_memorydb.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out

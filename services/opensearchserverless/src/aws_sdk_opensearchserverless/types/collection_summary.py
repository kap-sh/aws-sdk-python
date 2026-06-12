"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CollectionSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.collection_group_name
    import aws_sdk_opensearchserverless.types.collection_id
    import aws_sdk_opensearchserverless.types.collection_name
    import aws_sdk_opensearchserverless.types.collection_status


class CollectionSummary(TypedDict):
    id: NotRequired["aws_sdk_opensearchserverless.types.collection_id.CollectionId"]
    """<p>The unique identifier of the collection.</p>"""
    name: NotRequired[
        "aws_sdk_opensearchserverless.types.collection_name.CollectionName"
    ]
    """<p>The name of the collection.</p>"""
    status: NotRequired[
        "aws_sdk_opensearchserverless.types.collection_status.CollectionStatus"
    ]
    """<p>The current status of the collection.</p>"""
    arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the collection.</p>"""
    kms_key_arn: NotRequired["str"]
    """<p>The ARN of the Amazon Web Services Key Management Service key used to encrypt the collection.</p>"""
    collection_group_name: NotRequired[
        "aws_sdk_opensearchserverless.types.collection_group_name.CollectionGroupName"
    ]
    """<p>The name of the collection group that contains this collection.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CollectionSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        out["status"] = value["status"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "collection_group_name" in value:
        out["collectionGroupName"] = value["collection_group_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CollectionSummary:
    out: CollectionSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "status" in data:
        out["status"] = data["status"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if "collectionGroupName" in data:
        out["collection_group_name"] = data["collectionGroupName"]
    return out

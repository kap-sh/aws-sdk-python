"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#DeleteCollectionDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.collection_id
    import aws_sdk_opensearchserverless.types.collection_name
    import aws_sdk_opensearchserverless.types.collection_status
    import aws_sdk_opensearchserverless.types.deletion_protection


class DeleteCollectionDetail(TypedDict):
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
    deletion_protection: NotRequired[
        "aws_sdk_opensearchserverless.types.deletion_protection.DeletionProtection"
    ]
    """<p>Indicates whether deletion protection is <code>ENABLED</code> or <code>DISABLED</code> for the collection.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteCollectionDetail) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        out["status"] = value["status"]
    if "deletion_protection" in value:
        out["deletionProtection"] = value["deletion_protection"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteCollectionDetail:
    out: DeleteCollectionDetail = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "status" in data:
        out["status"] = data["status"]
    if "deletionProtection" in data:
        out["deletion_protection"] = data["deletionProtection"]
    return out

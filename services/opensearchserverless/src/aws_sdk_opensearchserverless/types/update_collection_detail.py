"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#UpdateCollectionDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.collection_id
    import aws_sdk_opensearchserverless.types.collection_name
    import aws_sdk_opensearchserverless.types.collection_status
    import aws_sdk_opensearchserverless.types.collection_type
    import aws_sdk_opensearchserverless.types.deletion_protection
    import aws_sdk_opensearchserverless.types.vector_options


class UpdateCollectionDetail(TypedDict, closed=True):
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
    type: NotRequired[
        "aws_sdk_opensearchserverless.types.collection_type.CollectionType"
    ]
    """<p>The collection type.</p>"""
    description: NotRequired["str"]
    """<p>The description of the collection.</p>"""
    vector_options: NotRequired[
        "aws_sdk_opensearchserverless.types.vector_options.VectorOptions"
    ]
    """<p>Configuration options for vector search capabilities in the collection.</p>"""
    arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the collection.</p>"""
    created_date: NotRequired["int"]
    """<p>The date and time when the collection was created.</p>"""
    last_modified_date: NotRequired["int"]
    """<p>The date and time when the collection was last modified.</p>"""
    deletion_protection: NotRequired[
        "aws_sdk_opensearchserverless.types.deletion_protection.DeletionProtection"
    ]
    """<p>Indicates whether deletion protection is <code>ENABLED</code> or <code>DISABLED</code> for the collection.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateCollectionDetail) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        out["status"] = value["status"]
    if "type" in value:
        out["type"] = value["type"]
    if "description" in value:
        out["description"] = value["description"]
    if "vector_options" in value:
        import aws_sdk_opensearchserverless.types.vector_options

        out["vectorOptions"] = (
            aws_sdk_opensearchserverless.types.vector_options.serialize_aws_json_1_0(
                value["vector_options"]
            )
        )
    if "arn" in value:
        out["arn"] = value["arn"]
    if "created_date" in value:
        out["createdDate"] = value["created_date"]
    if "last_modified_date" in value:
        out["lastModifiedDate"] = value["last_modified_date"]
    if "deletion_protection" in value:
        out["deletionProtection"] = value["deletion_protection"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateCollectionDetail:
    out: UpdateCollectionDetail = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "status" in data:
        out["status"] = data["status"]
    if "type" in data:
        out["type"] = data["type"]
    if "description" in data:
        out["description"] = data["description"]
    if "vectorOptions" in data:
        import aws_sdk_opensearchserverless.types.vector_options

        out["vector_options"] = (
            aws_sdk_opensearchserverless.types.vector_options.deserialize_aws_json_1_0(
                data["vectorOptions"]
            )
        )
    if "arn" in data:
        out["arn"] = data["arn"]
    if "createdDate" in data:
        out["created_date"] = data["createdDate"]
    if "lastModifiedDate" in data:
        out["last_modified_date"] = data["lastModifiedDate"]
    if "deletionProtection" in data:
        out["deletion_protection"] = data["deletionProtection"]
    return out

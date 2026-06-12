"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#UpdateCollectionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_opensearchserverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.client_token
    import aws_sdk_opensearchserverless.types.collection_id
    import aws_sdk_opensearchserverless.types.deletion_protection
    import aws_sdk_opensearchserverless.types.vector_options


class UpdateCollectionRequest(TypedDict):
    id: "aws_sdk_opensearchserverless.types.collection_id.CollectionId"
    """<p>The unique identifier of the collection.</p>"""
    description: NotRequired["str"]
    """<p>A description of the collection.</p>"""
    vector_options: NotRequired[
        "aws_sdk_opensearchserverless.types.vector_options.VectorOptions"
    ]
    """<p>Configuration options for vector search capabilities in the collection.</p>"""
    deletion_protection: NotRequired[
        "aws_sdk_opensearchserverless.types.deletion_protection.DeletionProtection"
    ]
    """<p>Indicates whether to enable or disable deletion protection for the collection. When set to <code>ENABLED</code>, the collection cannot be deleted.</p>"""
    client_token: NotRequired[
        "aws_sdk_opensearchserverless.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateCollectionRequest) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "description" in value:
        out["description"] = value["description"]
    if "vector_options" in value:
        import aws_sdk_opensearchserverless.types.vector_options

        out["vectorOptions"] = (
            aws_sdk_opensearchserverless.types.vector_options.serialize_aws_json_1_0(
                value["vector_options"]
            )
        )
    if "deletion_protection" in value:
        out["deletionProtection"] = value["deletion_protection"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateCollectionRequest:
    out: UpdateCollectionRequest = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("UpdateCollectionRequest.id required")
    if "description" in data:
        out["description"] = data["description"]
    if "vectorOptions" in data:
        import aws_sdk_opensearchserverless.types.vector_options

        out["vector_options"] = (
            aws_sdk_opensearchserverless.types.vector_options.deserialize_aws_json_1_0(
                data["vectorOptions"]
            )
        )
    if "deletionProtection" in data:
        out["deletion_protection"] = data["deletionProtection"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out

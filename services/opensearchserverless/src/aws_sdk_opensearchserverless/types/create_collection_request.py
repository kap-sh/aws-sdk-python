"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CreateCollectionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_opensearchserverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.client_token
    import aws_sdk_opensearchserverless.types.collection_group_name
    import aws_sdk_opensearchserverless.types.collection_name
    import aws_sdk_opensearchserverless.types.collection_type
    import aws_sdk_opensearchserverless.types.deletion_protection
    import aws_sdk_opensearchserverless.types.encryption_config
    import aws_sdk_opensearchserverless.types.standby_replicas
    import aws_sdk_opensearchserverless.types.tags
    import aws_sdk_opensearchserverless.types.vector_options


class CreateCollectionRequest(TypedDict):
    name: "aws_sdk_opensearchserverless.types.collection_name.CollectionName"
    """<p>Name of the collection.</p>"""
    type: NotRequired[
        "aws_sdk_opensearchserverless.types.collection_type.CollectionType"
    ]
    """<p>The type of collection.</p>"""
    description: NotRequired["str"]
    """<p>Description of the collection.</p>"""
    tags: NotRequired["aws_sdk_opensearchserverless.types.tags.Tags"]
    """<p>An arbitrary set of tags (key–value pairs) to associate with the OpenSearch Serverless collection.</p>"""
    standby_replicas: NotRequired[
        "aws_sdk_opensearchserverless.types.standby_replicas.StandbyReplicas"
    ]
    """<p>Indicates whether standby replicas should be used for a collection.</p>"""
    vector_options: NotRequired[
        "aws_sdk_opensearchserverless.types.vector_options.VectorOptions"
    ]
    """<p>Configuration options for vector search capabilities in the collection.</p>"""
    collection_group_name: NotRequired[
        "aws_sdk_opensearchserverless.types.collection_group_name.CollectionGroupName"
    ]
    """<p>The name of the collection group to associate with the collection.</p>"""
    encryption_config: NotRequired[
        "aws_sdk_opensearchserverless.types.encryption_config.EncryptionConfig"
    ]
    """<p>Encryption settings for the collection.</p>"""
    deletion_protection: NotRequired[
        "aws_sdk_opensearchserverless.types.deletion_protection.DeletionProtection"
    ]
    """<p>Indicates whether to enable deletion protection for the collection. When set to <code>ENABLED</code>, the collection cannot be deleted.</p>"""
    client_token: NotRequired[
        "aws_sdk_opensearchserverless.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateCollectionRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "type" in value:
        out["type"] = value["type"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import aws_sdk_opensearchserverless.types.tags

        out["tags"] = aws_sdk_opensearchserverless.types.tags.serialize_aws_json_1_0(
            value["tags"]
        )
    if "standby_replicas" in value:
        out["standbyReplicas"] = value["standby_replicas"]
    if "vector_options" in value:
        import aws_sdk_opensearchserverless.types.vector_options

        out["vectorOptions"] = (
            aws_sdk_opensearchserverless.types.vector_options.serialize_aws_json_1_0(
                value["vector_options"]
            )
        )
    if "collection_group_name" in value:
        out["collectionGroupName"] = value["collection_group_name"]
    if "encryption_config" in value:
        import aws_sdk_opensearchserverless.types.encryption_config

        out["encryptionConfig"] = (
            aws_sdk_opensearchserverless.types.encryption_config.serialize_aws_json_1_0(
                value["encryption_config"]
            )
        )
    if "deletion_protection" in value:
        out["deletionProtection"] = value["deletion_protection"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateCollectionRequest:
    out: CreateCollectionRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateCollectionRequest.name required")
    if "type" in data:
        out["type"] = data["type"]
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import aws_sdk_opensearchserverless.types.tags

        out["tags"] = aws_sdk_opensearchserverless.types.tags.deserialize_aws_json_1_0(
            data["tags"]
        )
    if "standbyReplicas" in data:
        out["standby_replicas"] = data["standbyReplicas"]
    if "vectorOptions" in data:
        import aws_sdk_opensearchserverless.types.vector_options

        out["vector_options"] = (
            aws_sdk_opensearchserverless.types.vector_options.deserialize_aws_json_1_0(
                data["vectorOptions"]
            )
        )
    if "collectionGroupName" in data:
        out["collection_group_name"] = data["collectionGroupName"]
    if "encryptionConfig" in data:
        import aws_sdk_opensearchserverless.types.encryption_config

        out["encryption_config"] = (
            aws_sdk_opensearchserverless.types.encryption_config.deserialize_aws_json_1_0(
                data["encryptionConfig"]
            )
        )
    if "deletionProtection" in data:
        out["deletion_protection"] = data["deletionProtection"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out

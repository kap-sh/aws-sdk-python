"""Generated from Smithy shape ``com.amazonaws.wisdom#CreateKnowledgeBaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wisdom.types.description
    import capo_wisdom.types.knowledge_base_type
    import capo_wisdom.types.name
    import capo_wisdom.types.non_empty_string
    import capo_wisdom.types.rendering_configuration
    import capo_wisdom.types.server_side_encryption_configuration
    import capo_wisdom.types.source_configuration
    import capo_wisdom.types.tags


class CreateKnowledgeBaseRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_wisdom.types.non_empty_string.NonEmptyString"]
    r"""<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>"""
    name: "capo_wisdom.types.name.Name"
    """<p>The name of the knowledge base.</p>"""
    knowledge_base_type: "capo_wisdom.types.knowledge_base_type.KnowledgeBaseType"
    """<p>The type of knowledge base. Only CUSTOM knowledge bases allow you to upload your own content. EXTERNAL knowledge bases support integrations with third-party systems whose content is synchronized automatically. </p>"""
    source_configuration: NotRequired[
        "capo_wisdom.types.source_configuration.SourceConfiguration"
    ]
    """<p>The source of the knowledge base content. Only set this argument for EXTERNAL knowledge bases.</p>"""
    rendering_configuration: NotRequired[
        "capo_wisdom.types.rendering_configuration.RenderingConfiguration"
    ]
    """<p>Information about how to render the content.</p>"""
    server_side_encryption_configuration: NotRequired[
        "capo_wisdom.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
    ]
    r"""<p>The configuration information for the customer managed key used for encryption. </p> <p>This KMS key must have a policy that allows <code>kms:CreateGrant</code>, <code>kms:DescribeKey</code>, and <code>kms:Decrypt/kms:GenerateDataKey</code> permissions to the IAM identity using the key to invoke Wisdom.</p> <p>For more information about setting up a customer managed key for Wisdom, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html\">Enable Amazon Connect Wisdom for your instance</a>.</p>"""
    description: NotRequired["capo_wisdom.types.description.Description"]
    """<p>The description.</p>"""
    tags: NotRequired["capo_wisdom.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateKnowledgeBaseRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["name"] = value["name"]
    out["knowledgeBaseType"] = value["knowledge_base_type"]
    if "source_configuration" in value:
        import capo_wisdom.types.source_configuration

        out["sourceConfiguration"] = (
            capo_wisdom.types.source_configuration.serialize_json(
                value["source_configuration"]
            )
        )
    if "rendering_configuration" in value:
        import capo_wisdom.types.rendering_configuration

        out["renderingConfiguration"] = (
            capo_wisdom.types.rendering_configuration.serialize_json(
                value["rendering_configuration"]
            )
        )
    if "server_side_encryption_configuration" in value:
        import capo_wisdom.types.server_side_encryption_configuration

        out["serverSideEncryptionConfiguration"] = (
            capo_wisdom.types.server_side_encryption_configuration.serialize_json(
                value["server_side_encryption_configuration"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_wisdom.types.tags

        out["tags"] = capo_wisdom.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateKnowledgeBaseRequest:
    out: CreateKnowledgeBaseRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateKnowledgeBaseRequest.name required")
    if "knowledgeBaseType" in data:
        out["knowledge_base_type"] = data["knowledgeBaseType"]
    else:
        raise DeserializationError(
            "CreateKnowledgeBaseRequest.knowledge_base_type required"
        )
    if "sourceConfiguration" in data:
        import capo_wisdom.types.source_configuration

        out["source_configuration"] = (
            capo_wisdom.types.source_configuration.deserialize_json(
                data["sourceConfiguration"]
            )
        )
    if "renderingConfiguration" in data:
        import capo_wisdom.types.rendering_configuration

        out["rendering_configuration"] = (
            capo_wisdom.types.rendering_configuration.deserialize_json(
                data["renderingConfiguration"]
            )
        )
    if "serverSideEncryptionConfiguration" in data:
        import capo_wisdom.types.server_side_encryption_configuration

        out["server_side_encryption_configuration"] = (
            capo_wisdom.types.server_side_encryption_configuration.deserialize_json(
                data["serverSideEncryptionConfiguration"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import capo_wisdom.types.tags

        out["tags"] = capo_wisdom.types.tags.deserialize_json(data["tags"])
    return out

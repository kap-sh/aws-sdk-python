"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#CreateSessionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.kms_key_arn
    import aws_sdk_bedrock_agent_runtime.types.session_metadata_map
    import aws_sdk_bedrock_agent_runtime.types.tags_map


class CreateSessionRequest(TypedDict):
    session_metadata: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.session_metadata_map.SessionMetadataMap"
    ]
    """<p>A map of key-value pairs containing attributes to be persisted across the session. For example, the user's ID, their language preference, and the type of device they are using.</p>"""
    encryption_key_arn: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.kms_key_arn.KmsKeyArn"
    ]
    r"""<p>The Amazon Resource Name (ARN) of the KMS key to use to encrypt the session data. The user or role creating the session must have permission to use the key. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/session-encryption.html\">Amazon Bedrock session encryption</a>. </p>"""
    tags: NotRequired["aws_sdk_bedrock_agent_runtime.types.tags_map.TagsMap"]
    """<p>Specify the key-value pairs for the tags that you want to attach to the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSessionRequest) -> dict:
    out: dict = {}
    if "session_metadata" in value:
        import aws_sdk_bedrock_agent_runtime.types.session_metadata_map

        out["sessionMetadata"] = (
            aws_sdk_bedrock_agent_runtime.types.session_metadata_map.serialize_json(
                value["session_metadata"]
            )
        )
    if "encryption_key_arn" in value:
        out["encryptionKeyArn"] = value["encryption_key_arn"]
    if "tags" in value:
        import aws_sdk_bedrock_agent_runtime.types.tags_map

        out["tags"] = aws_sdk_bedrock_agent_runtime.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateSessionRequest:
    out: CreateSessionRequest = {}  # type: ignore[typeddict-item]
    if "sessionMetadata" in data:
        import aws_sdk_bedrock_agent_runtime.types.session_metadata_map

        out["session_metadata"] = (
            aws_sdk_bedrock_agent_runtime.types.session_metadata_map.deserialize_json(
                data["sessionMetadata"]
            )
        )
    if "encryptionKeyArn" in data:
        out["encryption_key_arn"] = data["encryptionKeyArn"]
    if "tags" in data:
        import aws_sdk_bedrock_agent_runtime.types.tags_map

        out["tags"] = aws_sdk_bedrock_agent_runtime.types.tags_map.deserialize_json(
            data["tags"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ProxyCredentials``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.basic_auth


class _ProxyCredentials_basicAuth(TypedDict, closed=True):
    basicAuth: "aws_sdk_bedrock_agentcore.types.basic_auth.BasicAuth"


ProxyCredentials: TypeAlias = _ProxyCredentials_basicAuth


# --- restJson1 ser/de ---
def serialize_json(value: ProxyCredentials) -> dict:
    if "basicAuth" in value:
        import aws_sdk_bedrock_agentcore.types.basic_auth

        return {
            "basicAuth": aws_sdk_bedrock_agentcore.types.basic_auth.serialize_json(
                value["basicAuth"]
            )
        }
    else:
        raise SerializationError("ProxyCredentials: no variant present")


def deserialize_json(data: dict) -> ProxyCredentials:
    if "basicAuth" in data:
        import aws_sdk_bedrock_agentcore.types.basic_auth

        return {
            "basicAuth": aws_sdk_bedrock_agentcore.types.basic_auth.deserialize_json(
                data["basicAuth"]
            )
        }
    else:
        raise DeserializationError("ProxyCredentials: no recognized variant key")

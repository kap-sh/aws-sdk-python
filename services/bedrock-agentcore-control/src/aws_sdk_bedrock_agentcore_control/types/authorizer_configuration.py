"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AuthorizerConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError, SerializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.custom_jwt_authorizer_configuration

class _AuthorizerConfiguration_customJWTAuthorizer(TypedDict):
    customJWTAuthorizer: "aws_sdk_bedrock_agentcore_control.types.custom_jwt_authorizer_configuration.CustomJWTAuthorizerConfiguration"

AuthorizerConfiguration: TypeAlias = _AuthorizerConfiguration_customJWTAuthorizer

# --- restJson1 ser/de ---
def serialize_json(value: AuthorizerConfiguration) -> dict:
    if "customJWTAuthorizer" in value:
        import aws_sdk_bedrock_agentcore_control.types.custom_jwt_authorizer_configuration
        return {"customJWTAuthorizer": aws_sdk_bedrock_agentcore_control.types.custom_jwt_authorizer_configuration.serialize_json(value["customJWTAuthorizer"])}
    else:
        raise SerializationError("AuthorizerConfiguration: no variant present")


def deserialize_json(data: dict) -> AuthorizerConfiguration:
    if "customJWTAuthorizer" in data:
        import aws_sdk_bedrock_agentcore_control.types.custom_jwt_authorizer_configuration
        return {"customJWTAuthorizer": aws_sdk_bedrock_agentcore_control.types.custom_jwt_authorizer_configuration.deserialize_json(data["customJWTAuthorizer"])}
    else:
        raise DeserializationError("AuthorizerConfiguration: no recognized variant key")
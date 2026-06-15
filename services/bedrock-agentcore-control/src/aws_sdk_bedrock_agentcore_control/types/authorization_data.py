"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AuthorizationData``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.o_auth2_authorization_data


class _AuthorizationData_oauth2(TypedDict):
    oauth2: "aws_sdk_bedrock_agentcore_control.types.o_auth2_authorization_data.OAuth2AuthorizationData"


AuthorizationData: TypeAlias = _AuthorizationData_oauth2


# --- restJson1 ser/de ---
def serialize_json(value: AuthorizationData) -> dict:
    if "oauth2" in value:
        import aws_sdk_bedrock_agentcore_control.types.o_auth2_authorization_data

        return {
            "oauth2": aws_sdk_bedrock_agentcore_control.types.o_auth2_authorization_data.serialize_json(
                value["oauth2"]
            )
        }
    else:
        raise SerializationError("AuthorizationData: no variant present")


def deserialize_json(data: dict) -> AuthorizationData:
    if "oauth2" in data:
        import aws_sdk_bedrock_agentcore_control.types.o_auth2_authorization_data

        return {
            "oauth2": aws_sdk_bedrock_agentcore_control.types.o_auth2_authorization_data.deserialize_json(
                data["oauth2"]
            )
        }
    else:
        raise DeserializationError("AuthorizationData: no recognized variant key")

"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessGatewayOutboundAuth``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.o_auth_credential_provider


class _HarnessGatewayOutboundAuth_awsIam(TypedDict):
    awsIam: "None"


class _HarnessGatewayOutboundAuth_none(TypedDict):
    none: "None"


class _HarnessGatewayOutboundAuth_oauth(TypedDict):
    oauth: "aws_sdk_bedrock_agentcore_control.types.o_auth_credential_provider.OAuthCredentialProvider"


HarnessGatewayOutboundAuth: TypeAlias = (
    _HarnessGatewayOutboundAuth_awsIam
    | _HarnessGatewayOutboundAuth_none
    | _HarnessGatewayOutboundAuth_oauth
)


# --- restJson1 ser/de ---
def serialize_json(value: HarnessGatewayOutboundAuth) -> dict:
    if "awsIam" in value:
        return {"awsIam": {}}
    elif "none" in value:
        return {"none": {}}
    elif "oauth" in value:
        import aws_sdk_bedrock_agentcore_control.types.o_auth_credential_provider

        return {
            "oauth": aws_sdk_bedrock_agentcore_control.types.o_auth_credential_provider.serialize_json(
                value["oauth"]
            )
        }
    else:
        raise SerializationError("HarnessGatewayOutboundAuth: no variant present")


def deserialize_json(data: dict) -> HarnessGatewayOutboundAuth:
    if "awsIam" in data:
        return {"awsIam": None}
    elif "none" in data:
        return {"none": None}
    elif "oauth" in data:
        import aws_sdk_bedrock_agentcore_control.types.o_auth_credential_provider

        return {
            "oauth": aws_sdk_bedrock_agentcore_control.types.o_auth_credential_provider.deserialize_json(
                data["oauth"]
            )
        }
    else:
        raise DeserializationError(
            "HarnessGatewayOutboundAuth: no recognized variant key"
        )

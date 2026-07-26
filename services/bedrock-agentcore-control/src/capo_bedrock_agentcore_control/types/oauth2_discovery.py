"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Oauth2Discovery``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.discovery_url_type
    import capo_bedrock_agentcore_control.types.oauth2_authorization_server_metadata


class _Oauth2Discovery_discoveryUrl(TypedDict, closed=True):
    discoveryUrl: (
        "capo_bedrock_agentcore_control.types.discovery_url_type.DiscoveryUrlType"
    )


class _Oauth2Discovery_authorizationServerMetadata(TypedDict, closed=True):
    authorizationServerMetadata: "capo_bedrock_agentcore_control.types.oauth2_authorization_server_metadata.Oauth2AuthorizationServerMetadata"


Oauth2Discovery: TypeAlias = (
    _Oauth2Discovery_discoveryUrl | _Oauth2Discovery_authorizationServerMetadata
)


# --- restJson1 ser/de ---
def serialize_json(value: Oauth2Discovery) -> dict:
    if "discoveryUrl" in value:
        return {"discoveryUrl": value["discoveryUrl"]}
    elif "authorizationServerMetadata" in value:
        import capo_bedrock_agentcore_control.types.oauth2_authorization_server_metadata

        return {
            "authorizationServerMetadata": capo_bedrock_agentcore_control.types.oauth2_authorization_server_metadata.serialize_json(
                value["authorizationServerMetadata"]
            )
        }
    else:
        raise SerializationError("Oauth2Discovery: no variant present")


def deserialize_json(data: dict) -> Oauth2Discovery:
    if "discoveryUrl" in data:
        return {"discoveryUrl": data["discoveryUrl"]}
    elif "authorizationServerMetadata" in data:
        import capo_bedrock_agentcore_control.types.oauth2_authorization_server_metadata

        return {
            "authorizationServerMetadata": capo_bedrock_agentcore_control.types.oauth2_authorization_server_metadata.deserialize_json(
                data["authorizationServerMetadata"]
            )
        }
    else:
        raise DeserializationError("Oauth2Discovery: no recognized variant key")

"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SlackOauth2ProviderConfigOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.client_id_type
    import aws_sdk_bedrock_agentcore_control.types.oauth2_discovery


class SlackOauth2ProviderConfigOutput(TypedDict, closed=True):
    oauth_discovery: (
        "aws_sdk_bedrock_agentcore_control.types.oauth2_discovery.Oauth2Discovery"
    )
    """<p>The OAuth2 discovery information for the Slack provider.</p>"""
    client_id: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.client_id_type.ClientIdType"
    ]
    """<p>The client ID for the Slack OAuth2 provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlackOauth2ProviderConfigOutput) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.oauth2_discovery

    out["oauthDiscovery"] = (
        aws_sdk_bedrock_agentcore_control.types.oauth2_discovery.serialize_json(
            value["oauth_discovery"]
        )
    )
    if "client_id" in value:
        out["clientId"] = value["client_id"]
    return out


def deserialize_json(data: dict) -> SlackOauth2ProviderConfigOutput:
    out: SlackOauth2ProviderConfigOutput = {}  # type: ignore[typeddict-item]
    if "oauthDiscovery" in data:
        import aws_sdk_bedrock_agentcore_control.types.oauth2_discovery

        out["oauth_discovery"] = (
            aws_sdk_bedrock_agentcore_control.types.oauth2_discovery.deserialize_json(
                data["oauthDiscovery"]
            )
        )
    else:
        raise DeserializationError(
            "SlackOauth2ProviderConfigOutput.oauth_discovery required"
        )
    if "clientId" in data:
        out["client_id"] = data["clientId"]
    return out

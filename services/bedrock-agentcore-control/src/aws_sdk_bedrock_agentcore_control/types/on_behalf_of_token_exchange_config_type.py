"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#OnBehalfOfTokenExchangeConfigType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.on_behalf_of_token_exchange_grant_type_type
    import aws_sdk_bedrock_agentcore_control.types.token_exchange_grant_type_config_type


class OnBehalfOfTokenExchangeConfigType(TypedDict):
    grant_type: "aws_sdk_bedrock_agentcore_control.types.on_behalf_of_token_exchange_grant_type_type.OnBehalfOfTokenExchangeGrantTypeType"
    """<p>The grant type for the on-behalf-of token exchange.</p>"""
    token_exchange_grant_type_config: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.token_exchange_grant_type_config_type.TokenExchangeGrantTypeConfigType"
    ]
    """<p>Configuration specific to the TOKEN_EXCHANGE grant type (RFC 8693).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OnBehalfOfTokenExchangeConfigType) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.on_behalf_of_token_exchange_grant_type_type

    out["grantType"] = (
        aws_sdk_bedrock_agentcore_control.types.on_behalf_of_token_exchange_grant_type_type.serialize_json(
            value["grant_type"]
        )
    )
    if "token_exchange_grant_type_config" in value:
        import aws_sdk_bedrock_agentcore_control.types.token_exchange_grant_type_config_type

        out["tokenExchangeGrantTypeConfig"] = (
            aws_sdk_bedrock_agentcore_control.types.token_exchange_grant_type_config_type.serialize_json(
                value["token_exchange_grant_type_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> OnBehalfOfTokenExchangeConfigType:
    out: OnBehalfOfTokenExchangeConfigType = {}  # type: ignore[typeddict-item]
    if "grantType" in data:
        import aws_sdk_bedrock_agentcore_control.types.on_behalf_of_token_exchange_grant_type_type

        out["grant_type"] = (
            aws_sdk_bedrock_agentcore_control.types.on_behalf_of_token_exchange_grant_type_type.deserialize_json(
                data["grantType"]
            )
        )
    else:
        raise DeserializationError(
            "OnBehalfOfTokenExchangeConfigType.grant_type required"
        )
    if "tokenExchangeGrantTypeConfig" in data:
        import aws_sdk_bedrock_agentcore_control.types.token_exchange_grant_type_config_type

        out["token_exchange_grant_type_config"] = (
            aws_sdk_bedrock_agentcore_control.types.token_exchange_grant_type_config_type.deserialize_json(
                data["tokenExchangeGrantTypeConfig"]
            )
        )
    return out

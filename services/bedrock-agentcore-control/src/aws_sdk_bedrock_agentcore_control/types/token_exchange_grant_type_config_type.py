"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#TokenExchangeGrantTypeConfigType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.actor_token_content_type
    import aws_sdk_bedrock_agentcore_control.types.scopes_list_type


class TokenExchangeGrantTypeConfigType(TypedDict):
    actor_token_content: "aws_sdk_bedrock_agentcore_control.types.actor_token_content_type.ActorTokenContentType"
    """<p>The content type for the actor token in the token exchange.</p>"""
    actor_token_scopes: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.scopes_list_type.ScopesListType"
    ]
    """<p>The scopes for the actor token. Only valid when actorTokenContent is M2M.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TokenExchangeGrantTypeConfigType) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.actor_token_content_type

    out["actorTokenContent"] = (
        aws_sdk_bedrock_agentcore_control.types.actor_token_content_type.serialize_json(
            value["actor_token_content"]
        )
    )
    if "actor_token_scopes" in value:
        import aws_sdk_bedrock_agentcore_control.types.scopes_list_type

        out["actorTokenScopes"] = (
            aws_sdk_bedrock_agentcore_control.types.scopes_list_type.serialize_json(
                value["actor_token_scopes"]
            )
        )
    return out


def deserialize_json(data: dict) -> TokenExchangeGrantTypeConfigType:
    out: TokenExchangeGrantTypeConfigType = {}  # type: ignore[typeddict-item]
    if "actorTokenContent" in data:
        import aws_sdk_bedrock_agentcore_control.types.actor_token_content_type

        out["actor_token_content"] = (
            aws_sdk_bedrock_agentcore_control.types.actor_token_content_type.deserialize_json(
                data["actorTokenContent"]
            )
        )
    else:
        raise DeserializationError(
            "TokenExchangeGrantTypeConfigType.actor_token_content required"
        )
    if "actorTokenScopes" in data:
        import aws_sdk_bedrock_agentcore_control.types.scopes_list_type

        out["actor_token_scopes"] = (
            aws_sdk_bedrock_agentcore_control.types.scopes_list_type.deserialize_json(
                data["actorTokenScopes"]
            )
        )
    return out

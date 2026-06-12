"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DeleteBotAliasResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_alias_id
    import aws_sdk_lex_models_v2.types.bot_alias_status
    import aws_sdk_lex_models_v2.types.id


class DeleteBotAliasResponse(TypedDict):
    bot_alias_id: NotRequired["aws_sdk_lex_models_v2.types.bot_alias_id.BotAliasId"]
    """<p>The unique identifier of the bot alias to delete.</p>"""
    bot_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the bot that contains the alias to delete.</p>"""
    bot_alias_status: NotRequired[
        "aws_sdk_lex_models_v2.types.bot_alias_status.BotAliasStatus"
    ]
    """<p>The current status of the alias. The status is <code>Deleting</code> while the alias is in the process of being deleted. Once the alias is deleted, it will no longer appear in the list of aliases returned by the <code>ListBotAliases</code> operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBotAliasResponse) -> dict:
    out: dict = {}
    if "bot_alias_id" in value:
        out["botAliasId"] = value["bot_alias_id"]
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_alias_status" in value:
        import aws_sdk_lex_models_v2.types.bot_alias_status

        out["botAliasStatus"] = (
            aws_sdk_lex_models_v2.types.bot_alias_status.serialize_json(
                value["bot_alias_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteBotAliasResponse:
    out: DeleteBotAliasResponse = {}  # type: ignore[typeddict-item]
    if "botAliasId" in data:
        out["bot_alias_id"] = data["botAliasId"]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "botAliasStatus" in data:
        import aws_sdk_lex_models_v2.types.bot_alias_status

        out["bot_alias_status"] = (
            aws_sdk_lex_models_v2.types.bot_alias_status.deserialize_json(
                data["botAliasStatus"]
            )
        )
    return out

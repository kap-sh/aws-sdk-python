"""Generated from Smithy shape ``com.amazonaws.bedrockagent#LexFlowNodeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_lex_bot_alias_arn
    import capo_bedrock_agent.types.flow_lex_bot_locale_id


class LexFlowNodeConfiguration(TypedDict, closed=True):
    bot_alias_arn: "capo_bedrock_agent.types.flow_lex_bot_alias_arn.FlowLexBotAliasArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon Lex bot alias to invoke.</p>"""
    locale_id: "capo_bedrock_agent.types.flow_lex_bot_locale_id.FlowLexBotLocaleId"
    """<p>The Region to invoke the Amazon Lex bot in.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LexFlowNodeConfiguration) -> dict:
    out: dict = {}
    out["botAliasArn"] = value.get("bot_alias_arn", "")
    out["localeId"] = value.get("locale_id", "")
    return out


def deserialize_json(data: dict) -> LexFlowNodeConfiguration:
    out: LexFlowNodeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("botAliasArn") is not None:
        out["bot_alias_arn"] = data["botAliasArn"]
    else:
        out["bot_alias_arn"] = ""
    if data.get("localeId") is not None:
        out["locale_id"] = data["localeId"]
    else:
        out["locale_id"] = ""
    return out

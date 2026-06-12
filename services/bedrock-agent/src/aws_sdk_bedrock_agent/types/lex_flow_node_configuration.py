"""Generated from Smithy shape ``com.amazonaws.bedrockagent#LexFlowNodeConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_lex_bot_alias_arn
    import aws_sdk_bedrock_agent.types.flow_lex_bot_locale_id


class LexFlowNodeConfiguration(TypedDict):
    bot_alias_arn: (
        "aws_sdk_bedrock_agent.types.flow_lex_bot_alias_arn.FlowLexBotAliasArn"
    )
    """<p>The Amazon Resource Name (ARN) of the Amazon Lex bot alias to invoke.</p>"""
    locale_id: "aws_sdk_bedrock_agent.types.flow_lex_bot_locale_id.FlowLexBotLocaleId"
    """<p>The Region to invoke the Amazon Lex bot in.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LexFlowNodeConfiguration) -> dict:
    out: dict = {}
    out["botAliasArn"] = value.get("bot_alias_arn", "")
    out["localeId"] = value.get("locale_id", "")
    return out


def deserialize_json(data: dict) -> LexFlowNodeConfiguration:
    out: LexFlowNodeConfiguration = {}  # type: ignore[typeddict-item]
    if "botAliasArn" in data:
        out["bot_alias_arn"] = data["botAliasArn"]
    else:
        out["bot_alias_arn"] = ""
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    else:
        out["locale_id"] = ""
    return out

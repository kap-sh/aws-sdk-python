"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#BrowserSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.browser_summary

BrowserSummaries: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.browser_summary.BrowserSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: BrowserSummaries) -> list:
    import aws_sdk_bedrock_agentcore_control.types.browser_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.browser_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BrowserSummaries:
    import aws_sdk_bedrock_agentcore_control.types.browser_summary

    out: BrowserSummaries = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.browser_summary.deserialize_json(
                item
            )
        )
    return out

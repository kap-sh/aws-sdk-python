"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#BrowserProfileSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.browser_profile_summary

BrowserProfileSummaries: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.browser_profile_summary.BrowserProfileSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: BrowserProfileSummaries) -> list:
    import aws_sdk_bedrock_agentcore_control.types.browser_profile_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.browser_profile_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BrowserProfileSummaries:
    import aws_sdk_bedrock_agentcore_control.types.browser_profile_summary

    out: BrowserProfileSummaries = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.browser_profile_summary.deserialize_json(
                item
            )
        )
    return out

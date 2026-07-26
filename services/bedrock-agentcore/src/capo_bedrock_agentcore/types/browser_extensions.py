"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BrowserExtensions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.browser_extension

BrowserExtensions: TypeAlias = list[
    "capo_bedrock_agentcore.types.browser_extension.BrowserExtension"
]


# --- restJson1 ser/de ---
def serialize_json(value: BrowserExtensions) -> list:
    import capo_bedrock_agentcore.types.browser_extension

    out: list = []
    for item in value:
        out.append(capo_bedrock_agentcore.types.browser_extension.serialize_json(item))
    return out


def deserialize_json(data: list) -> BrowserExtensions:
    import capo_bedrock_agentcore.types.browser_extension

    out: BrowserExtensions = []
    for item in data:
        out.append(
            capo_bedrock_agentcore.types.browser_extension.deserialize_json(item)
        )
    return out

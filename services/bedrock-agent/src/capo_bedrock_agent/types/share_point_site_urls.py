"""Generated from Smithy shape ``com.amazonaws.bedrockagent#SharePointSiteUrls``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.https_url

SharePointSiteUrls: TypeAlias = list["capo_bedrock_agent.types.https_url.HttpsUrl"]


# --- restJson1 ser/de ---
def serialize_json(value: SharePointSiteUrls) -> list:
    return list(value)


def deserialize_json(data: list) -> SharePointSiteUrls:
    return [item for item in data if item is not None]

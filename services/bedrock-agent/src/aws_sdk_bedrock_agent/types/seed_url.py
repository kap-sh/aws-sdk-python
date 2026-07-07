"""Generated from Smithy shape ``com.amazonaws.bedrockagent#SeedUrl``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.url


class SeedUrl(TypedDict, closed=True):
    url: NotRequired["aws_sdk_bedrock_agent.types.url.Url"]
    """<p>A seed or starting point URL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SeedUrl) -> dict:
    out: dict = {}
    if "url" in value:
        out["url"] = value["url"]
    return out


def deserialize_json(data: dict) -> SeedUrl:
    out: SeedUrl = {}  # type: ignore[typeddict-item]
    if "url" in data:
        out["url"] = data["url"]
    return out

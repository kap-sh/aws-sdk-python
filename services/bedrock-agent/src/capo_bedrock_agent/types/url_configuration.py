"""Generated from Smithy shape ``com.amazonaws.bedrockagent#UrlConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.seed_urls


class UrlConfiguration(TypedDict, closed=True):
    seed_urls: NotRequired["capo_bedrock_agent.types.seed_urls.SeedUrls"]
    """<p>One or more seed or starting point URLs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UrlConfiguration) -> dict:
    out: dict = {}
    if "seed_urls" in value:
        import capo_bedrock_agent.types.seed_urls

        out["seedUrls"] = capo_bedrock_agent.types.seed_urls.serialize_json(
            value["seed_urls"]
        )
    return out


def deserialize_json(data: dict) -> UrlConfiguration:
    out: UrlConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("seedUrls") is not None:
        import capo_bedrock_agent.types.seed_urls

        out["seed_urls"] = capo_bedrock_agent.types.seed_urls.deserialize_json(
            data["seedUrls"]
        )
    return out

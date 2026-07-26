"""Generated from Smithy shape ``com.amazonaws.qconnect#UrlConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.seed_urls


class UrlConfiguration(TypedDict, closed=True):
    seed_urls: NotRequired["capo_qconnect.types.seed_urls.SeedUrls"]
    """<p>List of URLs for crawling.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UrlConfiguration) -> dict:
    out: dict = {}
    if "seed_urls" in value:
        import capo_qconnect.types.seed_urls

        out["seedUrls"] = capo_qconnect.types.seed_urls.serialize_json(
            value["seed_urls"]
        )
    return out


def deserialize_json(data: dict) -> UrlConfiguration:
    out: UrlConfiguration = {}  # type: ignore[typeddict-item]
    if "seedUrls" in data:
        import capo_qconnect.types.seed_urls

        out["seed_urls"] = capo_qconnect.types.seed_urls.deserialize_json(
            data["seedUrls"]
        )
    return out

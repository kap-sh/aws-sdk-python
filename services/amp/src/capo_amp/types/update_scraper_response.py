"""Generated from Smithy shape ``com.amazonaws.amp#UpdateScraperResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_amp.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amp.types.scraper_arn
    import capo_amp.types.scraper_id
    import capo_amp.types.scraper_status
    import capo_amp.types.tag_map


class UpdateScraperResponse(TypedDict, closed=True):
    scraper_id: "capo_amp.types.scraper_id.ScraperId"
    """<p>The ID of the updated scraper.</p>"""
    arn: "capo_amp.types.scraper_arn.ScraperArn"
    """<p>The Amazon Resource Name (ARN) of the updated scraper.</p>"""
    status: "capo_amp.types.scraper_status.ScraperStatus"
    """<p>A structure that displays the current status of the scraper.</p>"""
    tags: NotRequired["capo_amp.types.tag_map.TagMap"]
    """<p>The list of tag keys and values that are associated with the scraper.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateScraperResponse) -> dict:
    out: dict = {}
    out["scraperId"] = value["scraper_id"]
    out["arn"] = value["arn"]
    import capo_amp.types.scraper_status

    out["status"] = capo_amp.types.scraper_status.serialize_json(value["status"])
    if "tags" in value:
        import capo_amp.types.tag_map

        out["tags"] = capo_amp.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> UpdateScraperResponse:
    out: UpdateScraperResponse = {}  # type: ignore[typeddict-item]
    if "scraperId" in data:
        out["scraper_id"] = data["scraperId"]
    else:
        raise DeserializationError("UpdateScraperResponse.scraper_id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("UpdateScraperResponse.arn required")
    if "status" in data:
        import capo_amp.types.scraper_status

        out["status"] = capo_amp.types.scraper_status.deserialize_json(data["status"])
    else:
        raise DeserializationError("UpdateScraperResponse.status required")
    if "tags" in data:
        import capo_amp.types.tag_map

        out["tags"] = capo_amp.types.tag_map.deserialize_json(data["tags"])
    return out

"""Generated from Smithy shape ``com.amazonaws.amp#DeleteScraperResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_amp.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amp.types.scraper_id
    import aws_sdk_amp.types.scraper_status


class DeleteScraperResponse(TypedDict, closed=True):
    scraper_id: "aws_sdk_amp.types.scraper_id.ScraperId"
    """<p>The ID of the scraper to delete.</p>"""
    status: "aws_sdk_amp.types.scraper_status.ScraperStatus"
    """<p>The current status of the scraper.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteScraperResponse) -> dict:
    out: dict = {}
    out["scraperId"] = value["scraper_id"]
    import aws_sdk_amp.types.scraper_status

    out["status"] = aws_sdk_amp.types.scraper_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> DeleteScraperResponse:
    out: DeleteScraperResponse = {}  # type: ignore[typeddict-item]
    if "scraperId" in data:
        out["scraper_id"] = data["scraperId"]
    else:
        raise DeserializationError("DeleteScraperResponse.scraper_id required")
    if "status" in data:
        import aws_sdk_amp.types.scraper_status

        out["status"] = aws_sdk_amp.types.scraper_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("DeleteScraperResponse.status required")
    return out

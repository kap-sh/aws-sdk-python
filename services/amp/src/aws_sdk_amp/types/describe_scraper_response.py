"""Generated from Smithy shape ``com.amazonaws.amp#DescribeScraperResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_amp.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amp.types.scraper_description


class DescribeScraperResponse(TypedDict):
    scraper: "aws_sdk_amp.types.scraper_description.ScraperDescription"
    """<p>Contains details about the scraper.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeScraperResponse) -> dict:
    out: dict = {}
    import aws_sdk_amp.types.scraper_description

    out["scraper"] = aws_sdk_amp.types.scraper_description.serialize_json(
        value["scraper"]
    )
    return out


def deserialize_json(data: dict) -> DescribeScraperResponse:
    out: DescribeScraperResponse = {}  # type: ignore[typeddict-item]
    if "scraper" in data:
        import aws_sdk_amp.types.scraper_description

        out["scraper"] = aws_sdk_amp.types.scraper_description.deserialize_json(
            data["scraper"]
        )
    else:
        raise DeserializationError("DescribeScraperResponse.scraper required")
    return out

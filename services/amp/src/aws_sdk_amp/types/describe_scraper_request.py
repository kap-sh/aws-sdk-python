"""Generated from Smithy shape ``com.amazonaws.amp#DescribeScraperRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amp.types.scraper_id


class DescribeScraperRequest(TypedDict):
    scraper_id: "aws_sdk_amp.types.scraper_id.ScraperId"
    """<p>The ID of the scraper to describe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeScraperRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeScraperRequest:
    out: DescribeScraperRequest = {}  # type: ignore[typeddict-item]
    return out

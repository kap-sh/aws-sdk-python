"""Generated from Smithy shape ``com.amazonaws.amp#DescribeScraperLoggingConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amp.types.scraper_id


class DescribeScraperLoggingConfigurationRequest(TypedDict):
    scraper_id: "aws_sdk_amp.types.scraper_id.ScraperId"
    """<p>The ID of the scraper whose logging configuration will be described.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeScraperLoggingConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeScraperLoggingConfigurationRequest:
    out: DescribeScraperLoggingConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out

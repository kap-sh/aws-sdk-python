"""Generated from Smithy shape ``com.amazonaws.amp#ScraperSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_amp.types.scraper_summary

ScraperSummaryList: TypeAlias = list["aws_sdk_amp.types.scraper_summary.ScraperSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: ScraperSummaryList) -> list:
    import aws_sdk_amp.types.scraper_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_amp.types.scraper_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ScraperSummaryList:
    import aws_sdk_amp.types.scraper_summary

    out: ScraperSummaryList = []
    for item in data:
        out.append(aws_sdk_amp.types.scraper_summary.deserialize_json(item))
    return out

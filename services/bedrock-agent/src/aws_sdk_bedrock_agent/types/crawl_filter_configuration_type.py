"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CrawlFilterConfigurationType``."""

from typing import Literal, TypeAlias, cast

CrawlFilterConfigurationType: TypeAlias = Literal["PATTERN",]


# --- restJson1 ser/de ---
def serialize_json(value: CrawlFilterConfigurationType) -> str:
    return value


def deserialize_json(data: str) -> CrawlFilterConfigurationType:
    return cast(CrawlFilterConfigurationType, data)

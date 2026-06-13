"""Generated from Smithy shape ``com.amazonaws.amp#ScraperComponents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_amp.types.scraper_component

ScraperComponents: TypeAlias = list[
    "aws_sdk_amp.types.scraper_component.ScraperComponent"
]


# --- restJson1 ser/de ---
def serialize_json(value: ScraperComponents) -> list:
    import aws_sdk_amp.types.scraper_component

    out: list = []
    for item in value:
        out.append(aws_sdk_amp.types.scraper_component.serialize_json(item))
    return out


def deserialize_json(data: list) -> ScraperComponents:
    import aws_sdk_amp.types.scraper_component

    out: ScraperComponents = []
    for item in data:
        out.append(aws_sdk_amp.types.scraper_component.deserialize_json(item))
    return out

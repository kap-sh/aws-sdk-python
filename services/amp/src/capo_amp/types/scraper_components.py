"""Generated from Smithy shape ``com.amazonaws.amp#ScraperComponents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_amp.types.scraper_component

ScraperComponents: TypeAlias = list["capo_amp.types.scraper_component.ScraperComponent"]


# --- restJson1 ser/de ---
def serialize_json(value: ScraperComponents) -> list:
    import capo_amp.types.scraper_component

    out: list = []
    for item in value:
        out.append(capo_amp.types.scraper_component.serialize_json(item))
    return out


def deserialize_json(data: list) -> ScraperComponents:
    import capo_amp.types.scraper_component

    out: ScraperComponents = []
    for item in data:
        out.append(capo_amp.types.scraper_component.deserialize_json(item))
    return out

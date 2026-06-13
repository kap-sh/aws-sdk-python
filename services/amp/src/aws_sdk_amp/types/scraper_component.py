"""Generated from Smithy shape ``com.amazonaws.amp#ScraperComponent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_amp.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amp.types.component_config
    import aws_sdk_amp.types.scraper_component_type


class ScraperComponent(TypedDict):
    type: "aws_sdk_amp.types.scraper_component_type.ScraperComponentType"
    """<p>The type of the scraper component.</p>"""
    config: NotRequired["aws_sdk_amp.types.component_config.ComponentConfig"]
    """<p>The configuration settings for the scraper component.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScraperComponent) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    if "config" in value:
        import aws_sdk_amp.types.component_config

        out["config"] = aws_sdk_amp.types.component_config.serialize_json(
            value["config"]
        )
    return out


def deserialize_json(data: dict) -> ScraperComponent:
    out: ScraperComponent = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("ScraperComponent.type required")
    if "config" in data:
        import aws_sdk_amp.types.component_config

        out["config"] = aws_sdk_amp.types.component_config.deserialize_json(
            data["config"]
        )
    return out

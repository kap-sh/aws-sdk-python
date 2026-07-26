"""Generated from Smithy shape ``com.amazonaws.synthetics#BaseScreenshots``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_synthetics.types.base_screenshot

BaseScreenshots: TypeAlias = list[
    "capo_synthetics.types.base_screenshot.BaseScreenshot"
]


# --- restJson1 ser/de ---
def serialize_json(value: BaseScreenshots) -> list:
    import capo_synthetics.types.base_screenshot

    out: list = []
    for item in value:
        out.append(capo_synthetics.types.base_screenshot.serialize_json(item))
    return out


def deserialize_json(data: list) -> BaseScreenshots:
    import capo_synthetics.types.base_screenshot

    out: BaseScreenshots = []
    for item in data:
        out.append(capo_synthetics.types.base_screenshot.deserialize_json(item))
    return out

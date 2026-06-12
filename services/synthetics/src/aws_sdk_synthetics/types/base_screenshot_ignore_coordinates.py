"""Generated from Smithy shape ``com.amazonaws.synthetics#BaseScreenshotIgnoreCoordinates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.base_screenshot_config_ignore_coordinate

BaseScreenshotIgnoreCoordinates: TypeAlias = list[
    "aws_sdk_synthetics.types.base_screenshot_config_ignore_coordinate.BaseScreenshotConfigIgnoreCoordinate"
]


# --- restJson1 ser/de ---
def serialize_json(value: BaseScreenshotIgnoreCoordinates) -> list:
    return list(value)


def deserialize_json(data: list) -> BaseScreenshotIgnoreCoordinates:
    return list(data)

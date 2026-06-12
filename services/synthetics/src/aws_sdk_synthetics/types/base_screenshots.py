"""Generated from Smithy shape ``com.amazonaws.synthetics#BaseScreenshots``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.base_screenshot

BaseScreenshots: TypeAlias = list[
    "aws_sdk_synthetics.types.base_screenshot.BaseScreenshot"
]


# --- restJson1 ser/de ---
def serialize_json(value: BaseScreenshots) -> list:
    import aws_sdk_synthetics.types.base_screenshot

    out: list = []
    for item in value:
        out.append(aws_sdk_synthetics.types.base_screenshot.serialize_json(item))
    return out


def deserialize_json(data: list) -> BaseScreenshots:
    import aws_sdk_synthetics.types.base_screenshot

    out: BaseScreenshots = []
    for item in data:
        out.append(aws_sdk_synthetics.types.base_screenshot.deserialize_json(item))
    return out

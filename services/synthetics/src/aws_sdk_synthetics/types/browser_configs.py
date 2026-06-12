"""Generated from Smithy shape ``com.amazonaws.synthetics#BrowserConfigs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.browser_config

BrowserConfigs: TypeAlias = list[
    "aws_sdk_synthetics.types.browser_config.BrowserConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: BrowserConfigs) -> list:
    import aws_sdk_synthetics.types.browser_config

    out: list = []
    for item in value:
        out.append(aws_sdk_synthetics.types.browser_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> BrowserConfigs:
    import aws_sdk_synthetics.types.browser_config

    out: BrowserConfigs = []
    for item in data:
        out.append(aws_sdk_synthetics.types.browser_config.deserialize_json(item))
    return out

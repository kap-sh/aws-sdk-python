"""Generated from Smithy shape ``com.amazonaws.synthetics#BrowserConfigs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_synthetics.types.browser_config

BrowserConfigs: TypeAlias = list["capo_synthetics.types.browser_config.BrowserConfig"]


# --- restJson1 ser/de ---
def serialize_json(value: BrowserConfigs) -> list:
    import capo_synthetics.types.browser_config

    out: list = []
    for item in value:
        out.append(capo_synthetics.types.browser_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> BrowserConfigs:
    import capo_synthetics.types.browser_config

    out: BrowserConfigs = []
    for item in data:
        out.append(capo_synthetics.types.browser_config.deserialize_json(item))
    return out

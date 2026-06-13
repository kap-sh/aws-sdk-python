"""Generated from Smithy shape ``com.amazonaws.quicksight#PluginVisualItemsLimitConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.long


class PluginVisualItemsLimitConfiguration(TypedDict):
    items_limit: NotRequired["aws_sdk_quicksight.types.long.Long"]
    """<p>Determines how many values are be fetched at once.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PluginVisualItemsLimitConfiguration) -> dict:
    out: dict = {}
    if "items_limit" in value:
        out["ItemsLimit"] = value["items_limit"]
    return out


def deserialize_json(data: dict) -> PluginVisualItemsLimitConfiguration:
    out: PluginVisualItemsLimitConfiguration = {}  # type: ignore[typeddict-item]
    if "ItemsLimit" in data:
        out["items_limit"] = data["ItemsLimit"]
    return out

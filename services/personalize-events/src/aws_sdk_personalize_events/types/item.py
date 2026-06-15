"""Generated from Smithy shape ``com.amazonaws.personalizeevents#Item``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_personalize_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_personalize_events.types.string_type
    import aws_sdk_personalize_events.types.synthesized_json_item_properties


class Item(TypedDict):
    item_id: "aws_sdk_personalize_events.types.string_type.StringType"
    """<p>The ID associated with the item.</p>"""
    properties: NotRequired[
        "aws_sdk_personalize_events.types.synthesized_json_item_properties.SynthesizedJsonItemProperties"
    ]
    r"""<p>A string map of item-specific metadata. Each element in the map consists of a key-value pair. For example, <code>{\"numberOfRatings\": \"12\"}</code>.</p> <p>The keys use camel case names that match the fields in the schema for the Items dataset. In the previous example, the <code>numberOfRatings</code> matches the 'NUMBER_OF_RATINGS' field defined in the Items schema. For categorical string data, to include multiple categories for a single item, separate each category with a pipe separator (<code>|</code>). For example, <code>\\"Horror|Action\\"</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Item) -> dict:
    out: dict = {}
    out["itemId"] = value["item_id"]
    if "properties" in value:
        out["properties"] = value["properties"]
    return out


def deserialize_json(data: dict) -> Item:
    out: Item = {}  # type: ignore[typeddict-item]
    if "itemId" in data:
        out["item_id"] = data["itemId"]
    else:
        raise DeserializationError("Item.item_id required")
    if "properties" in data:
        out["properties"] = data["properties"]
    return out

"""Generated from Smithy shape ``com.amazonaws.mediastoredata#Item``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediastore_data.types.content_type
    import capo_mediastore_data.types.e_tag
    import capo_mediastore_data.types.item_name
    import capo_mediastore_data.types.item_type
    import capo_mediastore_data.types.non_negative_long
    import capo_mediastore_data.types.time_stamp


class Item(TypedDict, closed=True):
    name: NotRequired["capo_mediastore_data.types.item_name.ItemName"]
    """<p>The name of the item.</p>"""
    type: NotRequired["capo_mediastore_data.types.item_type.ItemType"]
    """<p>The item type (folder or object).</p>"""
    e_tag: NotRequired["capo_mediastore_data.types.e_tag.ETag"]
    """<p>The ETag that represents a unique instance of the item.</p>"""
    last_modified: NotRequired["capo_mediastore_data.types.time_stamp.TimeStamp"]
    """<p>The date and time that the item was last modified.</p>"""
    content_type: NotRequired["capo_mediastore_data.types.content_type.ContentType"]
    """<p>The content type of the item.</p>"""
    content_length: NotRequired[
        "capo_mediastore_data.types.non_negative_long.NonNegativeLong"
    ]
    """<p>The length of the item in bytes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Item) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        import capo_mediastore_data.types.item_type

        out["Type"] = capo_mediastore_data.types.item_type.serialize_json(value["type"])
    if "e_tag" in value:
        out["ETag"] = value["e_tag"]
    if "last_modified" in value:
        import capo_mediastore_data.types.time_stamp

        out["LastModified"] = capo_mediastore_data.types.time_stamp.serialize_json(
            value["last_modified"]
        )
    if "content_type" in value:
        out["ContentType"] = value["content_type"]
    if "content_length" in value:
        out["ContentLength"] = value["content_length"]
    return out


def deserialize_json(data: dict) -> Item:
    out: Item = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Type" in data:
        import capo_mediastore_data.types.item_type

        out["type"] = capo_mediastore_data.types.item_type.deserialize_json(
            data["Type"]
        )
    if "ETag" in data:
        out["e_tag"] = data["ETag"]
    if "LastModified" in data:
        import capo_mediastore_data.types.time_stamp

        out["last_modified"] = capo_mediastore_data.types.time_stamp.deserialize_json(
            data["LastModified"]
        )
    if "ContentType" in data:
        out["content_type"] = data["ContentType"]
    if "ContentLength" in data:
        out["content_length"] = data["ContentLength"]
    return out

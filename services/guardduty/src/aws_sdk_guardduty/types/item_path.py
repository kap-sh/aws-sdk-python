"""Generated from Smithy shape ``com.amazonaws.guardduty#ItemPath``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.string


class ItemPath(TypedDict, closed=True):
    nested_item_path: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The nested item path where the infected file was found.</p>"""
    hash: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The hash value of the infected resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ItemPath) -> dict:
    out: dict = {}
    if "nested_item_path" in value:
        out["nestedItemPath"] = value["nested_item_path"]
    if "hash" in value:
        out["hash"] = value["hash"]
    return out


def deserialize_json(data: dict) -> ItemPath:
    out: ItemPath = {}  # type: ignore[typeddict-item]
    if "nestedItemPath" in data:
        out["nested_item_path"] = data["nestedItemPath"]
    if "hash" in data:
        out["hash"] = data["hash"]
    return out

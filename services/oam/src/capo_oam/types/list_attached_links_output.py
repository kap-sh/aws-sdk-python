"""Generated from Smithy shape ``com.amazonaws.oam#ListAttachedLinksOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_oam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_oam.types.list_attached_links_items


class ListAttachedLinksOutput(TypedDict, closed=True):
    items: "capo_oam.types.list_attached_links_items.ListAttachedLinksItems"
    """<p>An array of structures that contain the information about the attached links.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to use when requesting the next set of links.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAttachedLinksOutput) -> dict:
    out: dict = {}
    import capo_oam.types.list_attached_links_items

    out["Items"] = capo_oam.types.list_attached_links_items.serialize_json(
        value["items"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAttachedLinksOutput:
    out: ListAttachedLinksOutput = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import capo_oam.types.list_attached_links_items

        out["items"] = capo_oam.types.list_attached_links_items.deserialize_json(
            data["Items"]
        )
    else:
        raise DeserializationError("ListAttachedLinksOutput.items required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

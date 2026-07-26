"""Generated from Smithy shape ``com.amazonaws.s3#Owner``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.display_name
    import capo_s3.types.id


class Owner(TypedDict, closed=True):
    display_name: NotRequired["capo_s3.types.display_name.DisplayName"]
    """<p></p>"""
    id: NotRequired["capo_s3.types.id.ID"]
    """<p>Container for the ID of the owner.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: Owner, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "display_name" in value:
        SubElement(el, "DisplayName").text = str(value["display_name"])
    if "id" in value:
        SubElement(el, "ID").text = str(value["id"])


def deserialize_xml(el: Element) -> Owner:
    out: Owner = {}  # type: ignore[typeddict-item]
    child_display_name = el.find("DisplayName")
    if child_display_name is not None:
        out["display_name"] = str(child_display_name.text or "")
    child_id = el.find("ID")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    return out

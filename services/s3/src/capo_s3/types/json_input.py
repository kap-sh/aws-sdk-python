"""Generated from Smithy shape ``com.amazonaws.s3#JSONInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.json_type


class JSONInput(TypedDict, closed=True):
    type: NotRequired["capo_s3.types.json_type.JSONType"]
    """<p>The type of JSON. Valid values: Document, Lines.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: JSONInput, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "type" in value:
        import capo_s3.types.json_type

        capo_s3.types.json_type.serialize_xml(value["type"], el, "Type")


def deserialize_xml(el: Element) -> JSONInput:
    out: JSONInput = {}  # type: ignore[typeddict-item]
    child_type = el.find("Type")
    if child_type is not None:
        import capo_s3.types.json_type

        out["type"] = capo_s3.types.json_type.deserialize_xml(child_type)
    return out

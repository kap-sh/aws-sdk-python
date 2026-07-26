"""Generated from Smithy shape ``com.amazonaws.s3control#MatchObjectSize``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.object_size_value


class MatchObjectSize(TypedDict, closed=True):
    bytes_greater_than: "capo_s3_control.types.object_size_value.ObjectSizeValue"
    """<p> Specifies the minimum object size in Bytes. The value must be a positive number, greater than 0 and less than 50 TB. </p>"""
    bytes_less_than: "capo_s3_control.types.object_size_value.ObjectSizeValue"
    """<p> Specifies the maximum object size in Bytes. The value must be a positive number, greater than the minimum object size and less than 50 TB. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: MatchObjectSize, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "BytesGreaterThan").text = str(value.get("bytes_greater_than", 0))
    SubElement(el, "BytesLessThan").text = str(value.get("bytes_less_than", 0))


def deserialize_xml(el: Element) -> MatchObjectSize:
    out: MatchObjectSize = {}  # type: ignore[typeddict-item]
    child_bytes_greater_than = el.find("BytesGreaterThan")
    if child_bytes_greater_than is not None:
        out["bytes_greater_than"] = int(child_bytes_greater_than.text or "")
    else:
        out["bytes_greater_than"] = 0
    child_bytes_less_than = el.find("BytesLessThan")
    if child_bytes_less_than is not None:
        out["bytes_less_than"] = int(child_bytes_less_than.text or "")
    else:
        out["bytes_less_than"] = 0
    return out

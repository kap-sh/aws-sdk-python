"""Generated from Smithy shape ``com.amazonaws.s3#CommonPrefix``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.prefix


class CommonPrefix(TypedDict, closed=True):
    prefix: NotRequired["aws_sdk_s3.types.prefix.Prefix"]
    """<p>Container for the specified common prefix.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CommonPrefix, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "prefix" in value:
        SubElement(el, "Prefix").text = str(value["prefix"])


def deserialize_xml(el: Element) -> CommonPrefix:
    out: CommonPrefix = {}  # type: ignore[typeddict-item]
    child_prefix = el.find("Prefix")
    if child_prefix is not None:
        out["prefix"] = str(child_prefix.text or "")
    return out

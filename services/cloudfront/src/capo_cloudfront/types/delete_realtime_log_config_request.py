"""Generated from Smithy shape ``com.amazonaws.cloudfront#DeleteRealtimeLogConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class DeleteRealtimeLogConfigRequest(TypedDict, closed=True):
    name: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The name of the real-time log configuration to delete.</p>"""
    arn: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The Amazon Resource Name (ARN) of the real-time log configuration to delete.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteRealtimeLogConfigRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "name" in value:
        SubElement(el, "Name").text = str(value["name"])
    if "arn" in value:
        SubElement(el, "ARN").text = str(value["arn"])


def deserialize_xml(el: Element) -> DeleteRealtimeLogConfigRequest:
    out: DeleteRealtimeLogConfigRequest = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_arn = el.find("ARN")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    return out

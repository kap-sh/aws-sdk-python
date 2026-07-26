"""Generated from Smithy shape ``com.amazonaws.route53#ChangeTagsForResourceResponse``."""

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement


class ChangeTagsForResourceResponse(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(
    value: ChangeTagsForResourceResponse, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ChangeTagsForResourceResponse:
    out: ChangeTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    return out

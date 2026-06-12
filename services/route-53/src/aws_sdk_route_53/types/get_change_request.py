"""Generated from Smithy shape ``com.amazonaws.route53#GetChangeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.change_id


class GetChangeRequest(TypedDict):
    id: "aws_sdk_route_53.types.change_id.ChangeId"
    """<p>The ID of the change batch request. The value that you specify here is the value that <code>ChangeResourceRecordSets</code> returned in the <code>Id</code> element when you submitted the request.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetChangeRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetChangeRequest:
    out: GetChangeRequest = {}  # type: ignore[typeddict-item]
    return out

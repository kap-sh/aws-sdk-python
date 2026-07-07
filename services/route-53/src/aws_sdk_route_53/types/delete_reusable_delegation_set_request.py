"""Generated from Smithy shape ``com.amazonaws.route53#DeleteReusableDelegationSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.resource_id


class DeleteReusableDelegationSetRequest(TypedDict, closed=True):
    id: "aws_sdk_route_53.types.resource_id.ResourceId"
    """<p>The ID of the reusable delegation set that you want to delete.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteReusableDelegationSetRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteReusableDelegationSetRequest:
    out: DeleteReusableDelegationSetRequest = {}  # type: ignore[typeddict-item]
    return out

"""Generated from Smithy shape ``com.amazonaws.route53#ChangeResourceRecordSetsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53.types.change_batch
    import aws_sdk_route_53.types.resource_id


class ChangeResourceRecordSetsRequest(TypedDict):
    hosted_zone_id: "aws_sdk_route_53.types.resource_id.ResourceId"
    """<p>The ID of the hosted zone that contains the resource record sets that you want to change.</p>"""
    change_batch: "aws_sdk_route_53.types.change_batch.ChangeBatch"
    """<p>A complex type that contains an optional comment and the <code>Changes</code> element.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ChangeResourceRecordSetsRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_route_53.types.change_batch

    aws_sdk_route_53.types.change_batch.serialize_xml(
        value["change_batch"], el, "ChangeBatch"
    )


def deserialize_xml(el: Element) -> ChangeResourceRecordSetsRequest:
    out: ChangeResourceRecordSetsRequest = {}  # type: ignore[typeddict-item]
    child_change_batch = el.find("ChangeBatch")
    if child_change_batch is not None:
        import aws_sdk_route_53.types.change_batch

        out["change_batch"] = aws_sdk_route_53.types.change_batch.deserialize_xml(
            child_change_batch
        )
    else:
        raise DeserializationError(
            "ChangeResourceRecordSetsRequest.change_batch required"
        )
    return out

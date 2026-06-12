"""Generated from Smithy shape ``com.amazonaws.route53#ChangeBatch``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53.types.changes
    import aws_sdk_route_53.types.resource_description


class ChangeBatch(TypedDict):
    comment: NotRequired[
        "aws_sdk_route_53.types.resource_description.ResourceDescription"
    ]
    """<p> <i>Optional:</i> Any comments you want to include about a change batch request.</p>"""
    changes: "aws_sdk_route_53.types.changes.Changes"
    """<p>Information about the changes to make to the record sets.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ChangeBatch, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "comment" in value:
        SubElement(el, "Comment").text = str(value["comment"])
    import aws_sdk_route_53.types.changes

    aws_sdk_route_53.types.changes.serialize_xml(value["changes"], el, "Changes")


def deserialize_xml(el: Element) -> ChangeBatch:
    out: ChangeBatch = {}  # type: ignore[typeddict-item]
    child_comment = el.find("Comment")
    if child_comment is not None:
        out["comment"] = str(child_comment.text or "")
    child_changes = el.find("Changes")
    if child_changes is not None:
        import aws_sdk_route_53.types.changes

        out["changes"] = aws_sdk_route_53.types.changes.deserialize_xml(child_changes)
    else:
        raise DeserializationError("ChangeBatch.changes required")
    return out

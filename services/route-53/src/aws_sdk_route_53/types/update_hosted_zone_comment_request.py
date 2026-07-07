"""Generated from Smithy shape ``com.amazonaws.route53#UpdateHostedZoneCommentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.resource_description
    import aws_sdk_route_53.types.resource_id


class UpdateHostedZoneCommentRequest(TypedDict, closed=True):
    id: "aws_sdk_route_53.types.resource_id.ResourceId"
    """<p>The ID for the hosted zone that you want to update the comment for.</p>"""
    comment: NotRequired[
        "aws_sdk_route_53.types.resource_description.ResourceDescription"
    ]
    """<p>The new comment for the hosted zone. If you don't specify a value for <code>Comment</code>, Amazon Route 53 deletes the existing value of the <code>Comment</code> element, if any.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: UpdateHostedZoneCommentRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "comment" in value:
        SubElement(el, "Comment").text = str(value["comment"])


def deserialize_xml(el: Element) -> UpdateHostedZoneCommentRequest:
    out: UpdateHostedZoneCommentRequest = {}  # type: ignore[typeddict-item]
    child_comment = el.find("Comment")
    if child_comment is not None:
        out["comment"] = str(child_comment.text or "")
    return out

"""Generated from Smithy shape ``com.amazonaws.route53#UpdateTrafficPolicyCommentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53.types.traffic_policy_comment
    import aws_sdk_route_53.types.traffic_policy_id
    import aws_sdk_route_53.types.traffic_policy_version


class UpdateTrafficPolicyCommentRequest(TypedDict):
    id: "aws_sdk_route_53.types.traffic_policy_id.TrafficPolicyId"
    """<p>The value of <code>Id</code> for the traffic policy that you want to update the comment for.</p>"""
    version: "aws_sdk_route_53.types.traffic_policy_version.TrafficPolicyVersion"
    """<p>The value of <code>Version</code> for the traffic policy that you want to update the comment for.</p>"""
    comment: "aws_sdk_route_53.types.traffic_policy_comment.TrafficPolicyComment"
    """<p>The new comment for the specified traffic policy and version.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: UpdateTrafficPolicyCommentRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Comment").text = str(value["comment"])


def deserialize_xml(el: Element) -> UpdateTrafficPolicyCommentRequest:
    out: UpdateTrafficPolicyCommentRequest = {}  # type: ignore[typeddict-item]
    child_comment = el.find("Comment")
    if child_comment is not None:
        out["comment"] = str(child_comment.text or "")
    else:
        raise DeserializationError("UpdateTrafficPolicyCommentRequest.comment required")
    return out

"""Generated from Smithy shape ``com.amazonaws.s3#RoutingRule``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3.types.condition
    import aws_sdk_s3.types.redirect


class RoutingRule(TypedDict):
    condition: NotRequired["aws_sdk_s3.types.condition.Condition"]
    """<p>A container for describing a condition that must be met for the specified redirect to apply. For example, 1. If request is for pages in the <code>/docs</code> folder, redirect to the <code>/documents</code> folder. 2. If request results in HTTP error 4xx, redirect request to another host where you might process the error.</p>"""
    redirect: "aws_sdk_s3.types.redirect.Redirect"
    """<p>Container for redirect information. You can redirect requests to another host, to another page, or with another protocol. In the event of an error, you can specify a different error code to return.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: RoutingRule, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "condition" in value:
        import aws_sdk_s3.types.condition

        aws_sdk_s3.types.condition.serialize_xml(value["condition"], el, "Condition")
    import aws_sdk_s3.types.redirect

    aws_sdk_s3.types.redirect.serialize_xml(value["redirect"], el, "Redirect")


def deserialize_xml(el: Element) -> RoutingRule:
    out: RoutingRule = {}  # type: ignore[typeddict-item]
    child_condition = el.find("Condition")
    if child_condition is not None:
        import aws_sdk_s3.types.condition

        out["condition"] = aws_sdk_s3.types.condition.deserialize_xml(child_condition)
    child_redirect = el.find("Redirect")
    if child_redirect is not None:
        import aws_sdk_s3.types.redirect

        out["redirect"] = aws_sdk_s3.types.redirect.deserialize_xml(child_redirect)
    else:
        raise DeserializationError("RoutingRule.redirect required")
    return out

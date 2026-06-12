"""Generated from Smithy shape ``com.amazonaws.cloudfront#WebAclCustomization``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.customization_action_type
    import aws_sdk_cloudfront.types.string


class WebAclCustomization(TypedDict):
    action: "aws_sdk_cloudfront.types.customization_action_type.CustomizationActionType"
    """<p>The action for the WAF web ACL customization. You can specify <code>override</code> to specify a separate WAF web ACL for the distribution tenant. If you specify <code>disable</code>, the distribution tenant won't have WAF web ACL protections and won't inherit from the multi-tenant distribution.</p>"""
    arn: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The Amazon Resource Name (ARN) of the WAF web ACL.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: WebAclCustomization, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_cloudfront.types.customization_action_type

    aws_sdk_cloudfront.types.customization_action_type.serialize_xml(
        value["action"], el, "Action"
    )
    if "arn" in value:
        SubElement(el, "Arn").text = str(value["arn"])


def deserialize_xml(el: Element) -> WebAclCustomization:
    out: WebAclCustomization = {}  # type: ignore[typeddict-item]
    child_action = el.find("Action")
    if child_action is not None:
        import aws_sdk_cloudfront.types.customization_action_type

        out["action"] = (
            aws_sdk_cloudfront.types.customization_action_type.deserialize_xml(
                child_action
            )
        )
    else:
        raise DeserializationError("WebAclCustomization.action required")
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    return out

"""Generated from Smithy shape ``com.amazonaws.cloudfront#PutResourcePolicyResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class PutResourcePolicyResult(TypedDict, closed=True):
    resource_arn: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The Amazon Resource Name (ARN) of the CloudFront resource for which the policy was created.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: PutResourcePolicyResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "resource_arn" in value:
        SubElement(el, "ResourceArn").text = str(value["resource_arn"])


def deserialize_xml(el: Element) -> PutResourcePolicyResult:
    out: PutResourcePolicyResult = {}  # type: ignore[typeddict-item]
    child_resource_arn = el.find("ResourceArn")
    if child_resource_arn is not None:
        out["resource_arn"] = str(child_resource_arn.text or "")
    return out

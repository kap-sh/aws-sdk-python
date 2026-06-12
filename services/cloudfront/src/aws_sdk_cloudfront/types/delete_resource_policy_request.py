"""Generated from Smithy shape ``com.amazonaws.cloudfront#DeleteResourcePolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class DeleteResourcePolicyRequest(TypedDict):
    resource_arn: "aws_sdk_cloudfront.types.string.string"
    """<p>The Amazon Resource Name (ARN) of the CloudFront resource for which the resource policy should be deleted.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteResourcePolicyRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "ResourceArn").text = str(value["resource_arn"])


def deserialize_xml(el: Element) -> DeleteResourcePolicyRequest:
    out: DeleteResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    child_resource_arn = el.find("ResourceArn")
    if child_resource_arn is not None:
        out["resource_arn"] = str(child_resource_arn.text or "")
    else:
        raise DeserializationError("DeleteResourcePolicyRequest.resource_arn required")
    return out

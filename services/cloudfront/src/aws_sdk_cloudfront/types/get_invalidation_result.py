"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetInvalidationResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.invalidation


class GetInvalidationResult(TypedDict):
    invalidation: NotRequired["aws_sdk_cloudfront.types.invalidation.Invalidation"]
    r"""<p>The invalidation's information. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/InvalidationDatatype.html\">Invalidation Complex Type</a>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetInvalidationResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "invalidation" in value:
        import aws_sdk_cloudfront.types.invalidation

        aws_sdk_cloudfront.types.invalidation.serialize_xml(
            value["invalidation"], el, "Invalidation"
        )


def deserialize_xml(el: Element) -> GetInvalidationResult:
    out: GetInvalidationResult = {}  # type: ignore[typeddict-item]
    child_invalidation = el.find("Invalidation")
    if child_invalidation is not None:
        import aws_sdk_cloudfront.types.invalidation

        out["invalidation"] = aws_sdk_cloudfront.types.invalidation.deserialize_xml(
            child_invalidation
        )
    return out

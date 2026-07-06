"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateInvalidationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.invalidation
    import aws_sdk_cloudfront.types.string


class CreateInvalidationResult(TypedDict, closed=True):
    location: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The fully qualified URI of the distribution and invalidation batch request, including the <code>Invalidation ID</code>.</p>"""
    invalidation: NotRequired["aws_sdk_cloudfront.types.invalidation.Invalidation"]
    """<p>The invalidation's information.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CreateInvalidationResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "invalidation" in value:
        import aws_sdk_cloudfront.types.invalidation

        aws_sdk_cloudfront.types.invalidation.serialize_xml(
            value["invalidation"], el, "Invalidation"
        )


def deserialize_xml(el: Element) -> CreateInvalidationResult:
    out: CreateInvalidationResult = {}  # type: ignore[typeddict-item]
    child_invalidation = el.find("Invalidation")
    if child_invalidation is not None:
        import aws_sdk_cloudfront.types.invalidation

        out["invalidation"] = aws_sdk_cloudfront.types.invalidation.deserialize_xml(
            child_invalidation
        )
    return out

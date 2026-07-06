"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateDistributionWithTagsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.distribution
    import aws_sdk_cloudfront.types.string


class CreateDistributionWithTagsResult(TypedDict, closed=True):
    distribution: NotRequired["aws_sdk_cloudfront.types.distribution.Distribution"]
    """<p>The distribution's information.</p>"""
    location: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The fully qualified URI of the new distribution resource just created.</p>"""
    e_tag: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The current version of the distribution created.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateDistributionWithTagsResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "distribution" in value:
        import aws_sdk_cloudfront.types.distribution

        aws_sdk_cloudfront.types.distribution.serialize_xml(
            value["distribution"], el, "Distribution"
        )


def deserialize_xml(el: Element) -> CreateDistributionWithTagsResult:
    out: CreateDistributionWithTagsResult = {}  # type: ignore[typeddict-item]
    child_distribution = el.find("Distribution")
    if child_distribution is not None:
        import aws_sdk_cloudfront.types.distribution

        out["distribution"] = aws_sdk_cloudfront.types.distribution.deserialize_xml(
            child_distribution
        )
    return out

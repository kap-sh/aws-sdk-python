"""Generated from Smithy shape ``com.amazonaws.cloudfront#CopyDistributionResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.distribution
    import aws_sdk_cloudfront.types.string


class CopyDistributionResult(TypedDict):
    distribution: NotRequired["aws_sdk_cloudfront.types.distribution.Distribution"]
    location: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The URL of the staging distribution.</p>"""
    e_tag: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The version identifier for the current version of the staging distribution.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CopyDistributionResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "distribution" in value:
        import aws_sdk_cloudfront.types.distribution

        aws_sdk_cloudfront.types.distribution.serialize_xml(
            value["distribution"], el, "Distribution"
        )


def deserialize_xml(el: Element) -> CopyDistributionResult:
    out: CopyDistributionResult = {}  # type: ignore[typeddict-item]
    child_distribution = el.find("Distribution")
    if child_distribution is not None:
        import aws_sdk_cloudfront.types.distribution

        out["distribution"] = aws_sdk_cloudfront.types.distribution.deserialize_xml(
            child_distribution
        )
    return out

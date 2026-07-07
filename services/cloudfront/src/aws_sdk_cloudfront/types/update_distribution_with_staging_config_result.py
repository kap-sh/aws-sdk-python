"""Generated from Smithy shape ``com.amazonaws.cloudfront#UpdateDistributionWithStagingConfigResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.distribution
    import aws_sdk_cloudfront.types.string


class UpdateDistributionWithStagingConfigResult(TypedDict, closed=True):
    distribution: NotRequired["aws_sdk_cloudfront.types.distribution.Distribution"]
    e_tag: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The current version of the primary distribution (after it's updated).</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: UpdateDistributionWithStagingConfigResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "distribution" in value:
        import aws_sdk_cloudfront.types.distribution

        aws_sdk_cloudfront.types.distribution.serialize_xml(
            value["distribution"], el, "Distribution"
        )


def deserialize_xml(el: Element) -> UpdateDistributionWithStagingConfigResult:
    out: UpdateDistributionWithStagingConfigResult = {}  # type: ignore[typeddict-item]
    child_distribution = el.find("Distribution")
    if child_distribution is not None:
        import aws_sdk_cloudfront.types.distribution

        out["distribution"] = aws_sdk_cloudfront.types.distribution.deserialize_xml(
            child_distribution
        )
    return out

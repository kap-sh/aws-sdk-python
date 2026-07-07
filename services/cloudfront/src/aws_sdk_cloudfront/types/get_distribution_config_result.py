"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetDistributionConfigResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.distribution_config
    import aws_sdk_cloudfront.types.string


class GetDistributionConfigResult(TypedDict, closed=True):
    distribution_config: NotRequired[
        "aws_sdk_cloudfront.types.distribution_config.DistributionConfig"
    ]
    """<p>The distribution's configuration information.</p>"""
    e_tag: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The current version of the configuration. For example: <code>E2QWRUHAPOMQZL</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetDistributionConfigResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "distribution_config" in value:
        import aws_sdk_cloudfront.types.distribution_config

        aws_sdk_cloudfront.types.distribution_config.serialize_xml(
            value["distribution_config"], el, "DistributionConfig"
        )


def deserialize_xml(el: Element) -> GetDistributionConfigResult:
    out: GetDistributionConfigResult = {}  # type: ignore[typeddict-item]
    child_distribution_config = el.find("DistributionConfig")
    if child_distribution_config is not None:
        import aws_sdk_cloudfront.types.distribution_config

        out["distribution_config"] = (
            aws_sdk_cloudfront.types.distribution_config.deserialize_xml(
                child_distribution_config
            )
        )
    return out

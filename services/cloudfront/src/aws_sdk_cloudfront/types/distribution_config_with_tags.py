"""Generated from Smithy shape ``com.amazonaws.cloudfront#DistributionConfigWithTags``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.distribution_config
    import aws_sdk_cloudfront.types.tags


class DistributionConfigWithTags(TypedDict):
    distribution_config: (
        "aws_sdk_cloudfront.types.distribution_config.DistributionConfig"
    )
    """<p>A distribution configuration.</p>"""
    tags: "aws_sdk_cloudfront.types.tags.Tags"
    """<p>A complex type that contains zero or more <code>Tag</code> elements.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: DistributionConfigWithTags, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_cloudfront.types.distribution_config

    aws_sdk_cloudfront.types.distribution_config.serialize_xml(
        value["distribution_config"], el, "DistributionConfig"
    )
    import aws_sdk_cloudfront.types.tags

    aws_sdk_cloudfront.types.tags.serialize_xml(value["tags"], el, "Tags")


def deserialize_xml(el: Element) -> DistributionConfigWithTags:
    out: DistributionConfigWithTags = {}  # type: ignore[typeddict-item]
    child_distribution_config = el.find("DistributionConfig")
    if child_distribution_config is not None:
        import aws_sdk_cloudfront.types.distribution_config

        out["distribution_config"] = (
            aws_sdk_cloudfront.types.distribution_config.deserialize_xml(
                child_distribution_config
            )
        )
    else:
        raise DeserializationError(
            "DistributionConfigWithTags.distribution_config required"
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_cloudfront.types.tags

        out["tags"] = aws_sdk_cloudfront.types.tags.deserialize_xml(child_tags)
    else:
        raise DeserializationError("DistributionConfigWithTags.tags required")
    return out

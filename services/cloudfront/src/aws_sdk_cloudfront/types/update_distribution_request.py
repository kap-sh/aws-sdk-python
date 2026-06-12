"""Generated from Smithy shape ``com.amazonaws.cloudfront#UpdateDistributionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.distribution_config
    import aws_sdk_cloudfront.types.string


class UpdateDistributionRequest(TypedDict):
    distribution_config: (
        "aws_sdk_cloudfront.types.distribution_config.DistributionConfig"
    )
    """<p>The distribution's configuration information.</p>"""
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The distribution's id.</p>"""
    if_match: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The value of the <code>ETag</code> header that you received when retrieving the distribution's configuration. For example: <code>E2QWRUHAPOMQZL</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: UpdateDistributionRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_cloudfront.types.distribution_config

    aws_sdk_cloudfront.types.distribution_config.serialize_xml(
        value["distribution_config"], el, "DistributionConfig"
    )


def deserialize_xml(el: Element) -> UpdateDistributionRequest:
    out: UpdateDistributionRequest = {}  # type: ignore[typeddict-item]
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
            "UpdateDistributionRequest.distribution_config required"
        )
    return out

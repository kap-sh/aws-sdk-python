"""Generated from Smithy shape ``com.amazonaws.cloudfront#UpdateCloudFrontOriginAccessIdentityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.cloud_front_origin_access_identity_config
    import aws_sdk_cloudfront.types.string


class UpdateCloudFrontOriginAccessIdentityRequest(TypedDict, closed=True):
    cloud_front_origin_access_identity_config: "aws_sdk_cloudfront.types.cloud_front_origin_access_identity_config.CloudFrontOriginAccessIdentityConfig"
    """<p>The identity's configuration information.</p>"""
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The identity's id.</p>"""
    if_match: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The value of the <code>ETag</code> header that you received when retrieving the identity's configuration. For example: <code>E2QWRUHAPOMQZL</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: UpdateCloudFrontOriginAccessIdentityRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_cloudfront.types.cloud_front_origin_access_identity_config

    aws_sdk_cloudfront.types.cloud_front_origin_access_identity_config.serialize_xml(
        value["cloud_front_origin_access_identity_config"],
        el,
        "CloudFrontOriginAccessIdentityConfig",
    )


def deserialize_xml(el: Element) -> UpdateCloudFrontOriginAccessIdentityRequest:
    out: UpdateCloudFrontOriginAccessIdentityRequest = {}  # type: ignore[typeddict-item]
    child_cloud_front_origin_access_identity_config = el.find(
        "CloudFrontOriginAccessIdentityConfig"
    )
    if child_cloud_front_origin_access_identity_config is not None:
        import aws_sdk_cloudfront.types.cloud_front_origin_access_identity_config

        out["cloud_front_origin_access_identity_config"] = (
            aws_sdk_cloudfront.types.cloud_front_origin_access_identity_config.deserialize_xml(
                child_cloud_front_origin_access_identity_config
            )
        )
    else:
        raise DeserializationError(
            "UpdateCloudFrontOriginAccessIdentityRequest.cloud_front_origin_access_identity_config required"
        )
    return out

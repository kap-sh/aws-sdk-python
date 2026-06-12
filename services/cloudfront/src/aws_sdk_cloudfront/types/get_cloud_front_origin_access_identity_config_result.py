"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetCloudFrontOriginAccessIdentityConfigResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.cloud_front_origin_access_identity_config
    import aws_sdk_cloudfront.types.string


class GetCloudFrontOriginAccessIdentityConfigResult(TypedDict):
    cloud_front_origin_access_identity_config: NotRequired[
        "aws_sdk_cloudfront.types.cloud_front_origin_access_identity_config.CloudFrontOriginAccessIdentityConfig"
    ]
    """<p>The origin access identity's configuration information.</p>"""
    e_tag: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The current version of the configuration. For example: <code>E2QWRUHAPOMQZL</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetCloudFrontOriginAccessIdentityConfigResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "cloud_front_origin_access_identity_config" in value:
        import aws_sdk_cloudfront.types.cloud_front_origin_access_identity_config

        aws_sdk_cloudfront.types.cloud_front_origin_access_identity_config.serialize_xml(
            value["cloud_front_origin_access_identity_config"],
            el,
            "CloudFrontOriginAccessIdentityConfig",
        )


def deserialize_xml(el: Element) -> GetCloudFrontOriginAccessIdentityConfigResult:
    out: GetCloudFrontOriginAccessIdentityConfigResult = {}  # type: ignore[typeddict-item]
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
    return out

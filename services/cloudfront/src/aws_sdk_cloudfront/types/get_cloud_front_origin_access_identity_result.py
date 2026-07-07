"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetCloudFrontOriginAccessIdentityResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.cloud_front_origin_access_identity
    import aws_sdk_cloudfront.types.string


class GetCloudFrontOriginAccessIdentityResult(TypedDict, closed=True):
    cloud_front_origin_access_identity: NotRequired[
        "aws_sdk_cloudfront.types.cloud_front_origin_access_identity.CloudFrontOriginAccessIdentity"
    ]
    """<p>The origin access identity's information.</p>"""
    e_tag: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The current version of the origin access identity's information. For example: <code>E2QWRUHAPOMQZL</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetCloudFrontOriginAccessIdentityResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "cloud_front_origin_access_identity" in value:
        import aws_sdk_cloudfront.types.cloud_front_origin_access_identity

        aws_sdk_cloudfront.types.cloud_front_origin_access_identity.serialize_xml(
            value["cloud_front_origin_access_identity"],
            el,
            "CloudFrontOriginAccessIdentity",
        )


def deserialize_xml(el: Element) -> GetCloudFrontOriginAccessIdentityResult:
    out: GetCloudFrontOriginAccessIdentityResult = {}  # type: ignore[typeddict-item]
    child_cloud_front_origin_access_identity = el.find("CloudFrontOriginAccessIdentity")
    if child_cloud_front_origin_access_identity is not None:
        import aws_sdk_cloudfront.types.cloud_front_origin_access_identity

        out["cloud_front_origin_access_identity"] = (
            aws_sdk_cloudfront.types.cloud_front_origin_access_identity.deserialize_xml(
                child_cloud_front_origin_access_identity
            )
        )
    return out

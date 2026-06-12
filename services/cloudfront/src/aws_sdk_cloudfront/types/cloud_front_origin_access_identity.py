"""Generated from Smithy shape ``com.amazonaws.cloudfront#CloudFrontOriginAccessIdentity``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.cloud_front_origin_access_identity_config
    import aws_sdk_cloudfront.types.string


class CloudFrontOriginAccessIdentity(TypedDict):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The ID for the origin access identity, for example, <code>E74FTE3AJFJ256A</code>. </p>"""
    s3_canonical_user_id: "aws_sdk_cloudfront.types.string.string"
    """<p>The Amazon S3 canonical user ID for the origin access identity, used when giving the origin access identity read permission to an object in Amazon S3.</p>"""
    cloud_front_origin_access_identity_config: NotRequired[
        "aws_sdk_cloudfront.types.cloud_front_origin_access_identity_config.CloudFrontOriginAccessIdentityConfig"
    ]
    """<p>The current configuration information for the identity.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CloudFrontOriginAccessIdentity, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    SubElement(el, "S3CanonicalUserId").text = str(value["s3_canonical_user_id"])
    if "cloud_front_origin_access_identity_config" in value:
        import aws_sdk_cloudfront.types.cloud_front_origin_access_identity_config

        aws_sdk_cloudfront.types.cloud_front_origin_access_identity_config.serialize_xml(
            value["cloud_front_origin_access_identity_config"],
            el,
            "CloudFrontOriginAccessIdentityConfig",
        )


def deserialize_xml(el: Element) -> CloudFrontOriginAccessIdentity:
    out: CloudFrontOriginAccessIdentity = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        raise DeserializationError("CloudFrontOriginAccessIdentity.id required")
    child_s3_canonical_user_id = el.find("S3CanonicalUserId")
    if child_s3_canonical_user_id is not None:
        out["s3_canonical_user_id"] = str(child_s3_canonical_user_id.text or "")
    else:
        raise DeserializationError(
            "CloudFrontOriginAccessIdentity.s3_canonical_user_id required"
        )
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

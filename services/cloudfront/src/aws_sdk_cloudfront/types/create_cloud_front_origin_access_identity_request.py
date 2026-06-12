"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateCloudFrontOriginAccessIdentityRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.cloud_front_origin_access_identity_config


class CreateCloudFrontOriginAccessIdentityRequest(TypedDict):
    cloud_front_origin_access_identity_config: "aws_sdk_cloudfront.types.cloud_front_origin_access_identity_config.CloudFrontOriginAccessIdentityConfig"
    """<p>The current configuration information for the identity.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateCloudFrontOriginAccessIdentityRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_cloudfront.types.cloud_front_origin_access_identity_config

    aws_sdk_cloudfront.types.cloud_front_origin_access_identity_config.serialize_xml(
        value["cloud_front_origin_access_identity_config"],
        el,
        "CloudFrontOriginAccessIdentityConfig",
    )


def deserialize_xml(el: Element) -> CreateCloudFrontOriginAccessIdentityRequest:
    out: CreateCloudFrontOriginAccessIdentityRequest = {}  # type: ignore[typeddict-item]
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
            "CreateCloudFrontOriginAccessIdentityRequest.cloud_front_origin_access_identity_config required"
        )
    return out

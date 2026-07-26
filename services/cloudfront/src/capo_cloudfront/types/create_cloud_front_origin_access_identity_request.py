"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateCloudFrontOriginAccessIdentityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.cloud_front_origin_access_identity_config


class CreateCloudFrontOriginAccessIdentityRequest(TypedDict, closed=True):
    cloud_front_origin_access_identity_config: "capo_cloudfront.types.cloud_front_origin_access_identity_config.CloudFrontOriginAccessIdentityConfig"
    """<p>The current configuration information for the identity.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateCloudFrontOriginAccessIdentityRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_cloudfront.types.cloud_front_origin_access_identity_config

    capo_cloudfront.types.cloud_front_origin_access_identity_config.serialize_xml(
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
        import capo_cloudfront.types.cloud_front_origin_access_identity_config

        out["cloud_front_origin_access_identity_config"] = (
            capo_cloudfront.types.cloud_front_origin_access_identity_config.deserialize_xml(
                child_cloud_front_origin_access_identity_config
            )
        )
    else:
        raise DeserializationError(
            "CreateCloudFrontOriginAccessIdentityRequest.cloud_front_origin_access_identity_config required"
        )
    return out

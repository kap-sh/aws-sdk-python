"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateCloudFrontOriginAccessIdentityResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.cloud_front_origin_access_identity
    import capo_cloudfront.types.string


class CreateCloudFrontOriginAccessIdentityResult(TypedDict, closed=True):
    cloud_front_origin_access_identity: NotRequired[
        "capo_cloudfront.types.cloud_front_origin_access_identity.CloudFrontOriginAccessIdentity"
    ]
    """<p>The origin access identity's information.</p>"""
    location: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The fully qualified URI of the new origin access identity just created.</p>"""
    e_tag: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The current version of the origin access identity created.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateCloudFrontOriginAccessIdentityResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "cloud_front_origin_access_identity" in value:
        import capo_cloudfront.types.cloud_front_origin_access_identity

        capo_cloudfront.types.cloud_front_origin_access_identity.serialize_xml(
            value["cloud_front_origin_access_identity"],
            el,
            "CloudFrontOriginAccessIdentity",
        )


def deserialize_xml(el: Element) -> CreateCloudFrontOriginAccessIdentityResult:
    out: CreateCloudFrontOriginAccessIdentityResult = {}  # type: ignore[typeddict-item]
    child_cloud_front_origin_access_identity = el.find("CloudFrontOriginAccessIdentity")
    if child_cloud_front_origin_access_identity is not None:
        import capo_cloudfront.types.cloud_front_origin_access_identity

        out["cloud_front_origin_access_identity"] = (
            capo_cloudfront.types.cloud_front_origin_access_identity.deserialize_xml(
                child_cloud_front_origin_access_identity
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListCloudFrontOriginAccessIdentitiesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.cloud_front_origin_access_identity_list


class ListCloudFrontOriginAccessIdentitiesResult(TypedDict):
    cloud_front_origin_access_identity_list: NotRequired[
        "aws_sdk_cloudfront.types.cloud_front_origin_access_identity_list.CloudFrontOriginAccessIdentityList"
    ]
    """<p>The <code>CloudFrontOriginAccessIdentityList</code> type.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListCloudFrontOriginAccessIdentitiesResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "cloud_front_origin_access_identity_list" in value:
        import aws_sdk_cloudfront.types.cloud_front_origin_access_identity_list

        aws_sdk_cloudfront.types.cloud_front_origin_access_identity_list.serialize_xml(
            value["cloud_front_origin_access_identity_list"],
            el,
            "CloudFrontOriginAccessIdentityList",
        )


def deserialize_xml(el: Element) -> ListCloudFrontOriginAccessIdentitiesResult:
    out: ListCloudFrontOriginAccessIdentitiesResult = {}  # type: ignore[typeddict-item]
    child_cloud_front_origin_access_identity_list = el.find(
        "CloudFrontOriginAccessIdentityList"
    )
    if child_cloud_front_origin_access_identity_list is not None:
        import aws_sdk_cloudfront.types.cloud_front_origin_access_identity_list

        out["cloud_front_origin_access_identity_list"] = (
            aws_sdk_cloudfront.types.cloud_front_origin_access_identity_list.deserialize_xml(
                child_cloud_front_origin_access_identity_list
            )
        )
    return out

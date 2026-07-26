"""Generated from Smithy shape ``com.amazonaws.cloudfront#CloudFrontOriginAccessIdentitySummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.cloud_front_origin_access_identity_summary

CloudFrontOriginAccessIdentitySummaryList: TypeAlias = list[
    "capo_cloudfront.types.cloud_front_origin_access_identity_summary.CloudFrontOriginAccessIdentitySummary"
]


# --- restXml ser/de ---
def serialize_xml(
    value: CloudFrontOriginAccessIdentitySummaryList, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_cloudfront.types.cloud_front_origin_access_identity_summary

        capo_cloudfront.types.cloud_front_origin_access_identity_summary.serialize_xml(
            item, el, "CloudFrontOriginAccessIdentitySummary"
        )


def deserialize_xml(el: Element) -> CloudFrontOriginAccessIdentitySummaryList:
    import capo_cloudfront.types.cloud_front_origin_access_identity_summary

    out: CloudFrontOriginAccessIdentitySummaryList = []
    for child in el.findall("CloudFrontOriginAccessIdentitySummary"):
        out.append(
            capo_cloudfront.types.cloud_front_origin_access_identity_summary.deserialize_xml(
                child
            )
        )
    return out


def serialize_xml_flat(
    value: CloudFrontOriginAccessIdentitySummaryList, parent: Element, tag: str
) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import capo_cloudfront.types.cloud_front_origin_access_identity_summary

        capo_cloudfront.types.cloud_front_origin_access_identity_summary.serialize_xml(
            item, parent, tag
        )


def deserialize_xml_flat(
    parent: Element, tag: str
) -> CloudFrontOriginAccessIdentitySummaryList:
    import capo_cloudfront.types.cloud_front_origin_access_identity_summary

    out: CloudFrontOriginAccessIdentitySummaryList = []
    for child in parent.findall(tag):
        out.append(
            capo_cloudfront.types.cloud_front_origin_access_identity_summary.deserialize_xml(
                child
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginRequestPolicySummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.origin_request_policy_summary

OriginRequestPolicySummaryList: TypeAlias = list[
    "aws_sdk_cloudfront.types.origin_request_policy_summary.OriginRequestPolicySummary"
]


# --- restXml ser/de ---
def serialize_xml(
    value: OriginRequestPolicySummaryList, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_cloudfront.types.origin_request_policy_summary

        aws_sdk_cloudfront.types.origin_request_policy_summary.serialize_xml(
            item, el, "OriginRequestPolicySummary"
        )


def deserialize_xml(el: Element) -> OriginRequestPolicySummaryList:
    import aws_sdk_cloudfront.types.origin_request_policy_summary

    out: OriginRequestPolicySummaryList = []
    for child in el.findall("OriginRequestPolicySummary"):
        out.append(
            aws_sdk_cloudfront.types.origin_request_policy_summary.deserialize_xml(
                child
            )
        )
    return out


def serialize_xml_flat(
    value: OriginRequestPolicySummaryList, parent: Element, tag: str
) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_cloudfront.types.origin_request_policy_summary

        aws_sdk_cloudfront.types.origin_request_policy_summary.serialize_xml(
            item, parent, tag
        )


def deserialize_xml_flat(parent: Element, tag: str) -> OriginRequestPolicySummaryList:
    import aws_sdk_cloudfront.types.origin_request_policy_summary

    out: OriginRequestPolicySummaryList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudfront.types.origin_request_policy_summary.deserialize_xml(
                child
            )
        )
    return out

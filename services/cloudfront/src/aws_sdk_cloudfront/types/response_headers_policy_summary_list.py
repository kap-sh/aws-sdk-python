"""Generated from Smithy shape ``com.amazonaws.cloudfront#ResponseHeadersPolicySummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.response_headers_policy_summary

ResponseHeadersPolicySummaryList: TypeAlias = list[
    "aws_sdk_cloudfront.types.response_headers_policy_summary.ResponseHeadersPolicySummary"
]


# --- restXml ser/de ---
def serialize_xml(
    value: ResponseHeadersPolicySummaryList, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_cloudfront.types.response_headers_policy_summary

        aws_sdk_cloudfront.types.response_headers_policy_summary.serialize_xml(
            item, el, "ResponseHeadersPolicySummary"
        )


def deserialize_xml(el: Element) -> ResponseHeadersPolicySummaryList:
    import aws_sdk_cloudfront.types.response_headers_policy_summary

    out: ResponseHeadersPolicySummaryList = []
    for child in el.findall("ResponseHeadersPolicySummary"):
        out.append(
            aws_sdk_cloudfront.types.response_headers_policy_summary.deserialize_xml(
                child
            )
        )
    return out


def serialize_xml_flat(
    value: ResponseHeadersPolicySummaryList, parent: Element, tag: str
) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_cloudfront.types.response_headers_policy_summary

        aws_sdk_cloudfront.types.response_headers_policy_summary.serialize_xml(
            item, parent, tag
        )


def deserialize_xml_flat(parent: Element, tag: str) -> ResponseHeadersPolicySummaryList:
    import aws_sdk_cloudfront.types.response_headers_policy_summary

    out: ResponseHeadersPolicySummaryList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudfront.types.response_headers_policy_summary.deserialize_xml(
                child
            )
        )
    return out

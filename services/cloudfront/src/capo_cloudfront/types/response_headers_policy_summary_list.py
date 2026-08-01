"""Generated from Smithy shape ``com.amazonaws.cloudfront#ResponseHeadersPolicySummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.response_headers_policy_summary

ResponseHeadersPolicySummaryList: TypeAlias = list[
    "capo_cloudfront.types.response_headers_policy_summary.ResponseHeadersPolicySummary"
]


# --- restXml ser/de ---
def serialize_xml(
    value: ResponseHeadersPolicySummaryList, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_cloudfront.types.response_headers_policy_summary

        capo_cloudfront.types.response_headers_policy_summary.serialize_xml(
            item, el, "ResponseHeadersPolicySummary"
        )


def deserialize_xml(el: Element) -> ResponseHeadersPolicySummaryList:
    import capo_cloudfront.types.response_headers_policy_summary

    out: ResponseHeadersPolicySummaryList = []
    for child in el.findall("ResponseHeadersPolicySummary"):
        out.append(
            capo_cloudfront.types.response_headers_policy_summary.deserialize_xml(child)
        )
    return out


def serialize_xml_flat(
    value: ResponseHeadersPolicySummaryList, parent: Element, tag: str
) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_cloudfront.types.response_headers_policy_summary

        capo_cloudfront.types.response_headers_policy_summary.serialize_xml(
            item, parent, tag
        )


def deserialize_xml_flat(parent: Element, tag: str) -> ResponseHeadersPolicySummaryList:
    import capo_cloudfront.types.response_headers_policy_summary

    out: ResponseHeadersPolicySummaryList = []
    for child in parent.findall(tag):
        out.append(
            capo_cloudfront.types.response_headers_policy_summary.deserialize_xml(child)
        )
    return out

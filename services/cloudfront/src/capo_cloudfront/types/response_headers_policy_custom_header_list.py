"""Generated from Smithy shape ``com.amazonaws.cloudfront#ResponseHeadersPolicyCustomHeaderList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.response_headers_policy_custom_header

ResponseHeadersPolicyCustomHeaderList: TypeAlias = list[
    "capo_cloudfront.types.response_headers_policy_custom_header.ResponseHeadersPolicyCustomHeader"
]


# --- restXml ser/de ---
def serialize_xml(
    value: ResponseHeadersPolicyCustomHeaderList, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_cloudfront.types.response_headers_policy_custom_header

        capo_cloudfront.types.response_headers_policy_custom_header.serialize_xml(
            item, el, "ResponseHeadersPolicyCustomHeader"
        )


def deserialize_xml(el: Element) -> ResponseHeadersPolicyCustomHeaderList:
    import capo_cloudfront.types.response_headers_policy_custom_header

    out: ResponseHeadersPolicyCustomHeaderList = []
    for child in el.findall("ResponseHeadersPolicyCustomHeader"):
        out.append(
            capo_cloudfront.types.response_headers_policy_custom_header.deserialize_xml(
                child
            )
        )
    return out


def serialize_xml_flat(
    value: ResponseHeadersPolicyCustomHeaderList, parent: Element, tag: str
) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import capo_cloudfront.types.response_headers_policy_custom_header

        capo_cloudfront.types.response_headers_policy_custom_header.serialize_xml(
            item, parent, tag
        )


def deserialize_xml_flat(
    parent: Element, tag: str
) -> ResponseHeadersPolicyCustomHeaderList:
    import capo_cloudfront.types.response_headers_policy_custom_header

    out: ResponseHeadersPolicyCustomHeaderList = []
    for child in parent.findall(tag):
        out.append(
            capo_cloudfront.types.response_headers_policy_custom_header.deserialize_xml(
                child
            )
        )
    return out

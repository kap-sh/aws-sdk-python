"""Generated from Smithy shape ``com.amazonaws.cloudfront#ResponseHeadersPolicyRemoveHeaderList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.response_headers_policy_remove_header

ResponseHeadersPolicyRemoveHeaderList: TypeAlias = list[
    "capo_cloudfront.types.response_headers_policy_remove_header.ResponseHeadersPolicyRemoveHeader"
]


# --- restXml ser/de ---
def serialize_xml(
    value: ResponseHeadersPolicyRemoveHeaderList, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_cloudfront.types.response_headers_policy_remove_header

        capo_cloudfront.types.response_headers_policy_remove_header.serialize_xml(
            item, el, "ResponseHeadersPolicyRemoveHeader"
        )


def deserialize_xml(el: Element) -> ResponseHeadersPolicyRemoveHeaderList:
    import capo_cloudfront.types.response_headers_policy_remove_header

    out: ResponseHeadersPolicyRemoveHeaderList = []
    for child in el.findall("ResponseHeadersPolicyRemoveHeader"):
        out.append(
            capo_cloudfront.types.response_headers_policy_remove_header.deserialize_xml(
                child
            )
        )
    return out


def serialize_xml_flat(
    value: ResponseHeadersPolicyRemoveHeaderList, parent: Element, tag: str
) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import capo_cloudfront.types.response_headers_policy_remove_header

        capo_cloudfront.types.response_headers_policy_remove_header.serialize_xml(
            item, parent, tag
        )


def deserialize_xml_flat(
    parent: Element, tag: str
) -> ResponseHeadersPolicyRemoveHeaderList:
    import capo_cloudfront.types.response_headers_policy_remove_header

    out: ResponseHeadersPolicyRemoveHeaderList = []
    for child in parent.findall(tag):
        out.append(
            capo_cloudfront.types.response_headers_policy_remove_header.deserialize_xml(
                child
            )
        )
    return out

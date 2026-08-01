"""Generated from Smithy shape ``com.amazonaws.cloudfront#CustomErrorResponseList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.custom_error_response

CustomErrorResponseList: TypeAlias = list[
    "capo_cloudfront.types.custom_error_response.CustomErrorResponse"
]


# --- restXml ser/de ---
def serialize_xml(value: CustomErrorResponseList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_cloudfront.types.custom_error_response

        capo_cloudfront.types.custom_error_response.serialize_xml(
            item, el, "CustomErrorResponse"
        )


def deserialize_xml(el: Element) -> CustomErrorResponseList:
    import capo_cloudfront.types.custom_error_response

    out: CustomErrorResponseList = []
    for child in el.findall("CustomErrorResponse"):
        out.append(capo_cloudfront.types.custom_error_response.deserialize_xml(child))
    return out


def serialize_xml_flat(
    value: CustomErrorResponseList, parent: Element, tag: str
) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_cloudfront.types.custom_error_response

        capo_cloudfront.types.custom_error_response.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> CustomErrorResponseList:
    import capo_cloudfront.types.custom_error_response

    out: CustomErrorResponseList = []
    for child in parent.findall(tag):
        out.append(capo_cloudfront.types.custom_error_response.deserialize_xml(child))
    return out

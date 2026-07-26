"""Generated from Smithy shape ``com.amazonaws.cloudfront#ValidationTokenDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.validation_token_detail

ValidationTokenDetailList: TypeAlias = list[
    "capo_cloudfront.types.validation_token_detail.ValidationTokenDetail"
]


# --- restXml ser/de ---
def serialize_xml(value: ValidationTokenDetailList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_cloudfront.types.validation_token_detail

        capo_cloudfront.types.validation_token_detail.serialize_xml(item, el, "member")


def deserialize_xml(el: Element) -> ValidationTokenDetailList:
    import capo_cloudfront.types.validation_token_detail

    out: ValidationTokenDetailList = []
    for child in el.findall("member"):
        out.append(capo_cloudfront.types.validation_token_detail.deserialize_xml(child))
    return out


def serialize_xml_flat(
    value: ValidationTokenDetailList, parent: Element, tag: str
) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import capo_cloudfront.types.validation_token_detail

        capo_cloudfront.types.validation_token_detail.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> ValidationTokenDetailList:
    import capo_cloudfront.types.validation_token_detail

    out: ValidationTokenDetailList = []
    for child in parent.findall(tag):
        out.append(capo_cloudfront.types.validation_token_detail.deserialize_xml(child))
    return out

"""Generated from Smithy shape ``com.amazonaws.s3#IntelligentTieringConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.intelligent_tiering_configuration

IntelligentTieringConfigurationList: TypeAlias = list[
    "capo_s3.types.intelligent_tiering_configuration.IntelligentTieringConfiguration"
]


# --- restXml ser/de ---
def serialize_xml(
    value: IntelligentTieringConfigurationList, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_s3.types.intelligent_tiering_configuration

        capo_s3.types.intelligent_tiering_configuration.serialize_xml(
            item, el, "member"
        )


def deserialize_xml(el: Element) -> IntelligentTieringConfigurationList:
    import capo_s3.types.intelligent_tiering_configuration

    out: IntelligentTieringConfigurationList = []
    for child in el.findall("member"):
        out.append(
            capo_s3.types.intelligent_tiering_configuration.deserialize_xml(child)
        )
    return out


def serialize_xml_flat(
    value: IntelligentTieringConfigurationList, parent: Element, tag: str
) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_s3.types.intelligent_tiering_configuration

        capo_s3.types.intelligent_tiering_configuration.serialize_xml(item, parent, tag)


def deserialize_xml_flat(
    parent: Element, tag: str
) -> IntelligentTieringConfigurationList:
    import capo_s3.types.intelligent_tiering_configuration

    out: IntelligentTieringConfigurationList = []
    for child in parent.findall(tag):
        out.append(
            capo_s3.types.intelligent_tiering_configuration.deserialize_xml(child)
        )
    return out

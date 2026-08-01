"""Generated from Smithy shape ``com.amazonaws.s3#TopicConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.topic_configuration

TopicConfigurationList: TypeAlias = list[
    "capo_s3.types.topic_configuration.TopicConfiguration"
]


# --- restXml ser/de ---
def serialize_xml(value: TopicConfigurationList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_s3.types.topic_configuration

        capo_s3.types.topic_configuration.serialize_xml(item, el, "member")


def deserialize_xml(el: Element) -> TopicConfigurationList:
    import capo_s3.types.topic_configuration

    out: TopicConfigurationList = []
    for child in el.findall("member"):
        out.append(capo_s3.types.topic_configuration.deserialize_xml(child))
    return out


def serialize_xml_flat(
    value: TopicConfigurationList, parent: Element, tag: str
) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_s3.types.topic_configuration

        capo_s3.types.topic_configuration.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> TopicConfigurationList:
    import capo_s3.types.topic_configuration

    out: TopicConfigurationList = []
    for child in parent.findall(tag):
        out.append(capo_s3.types.topic_configuration.deserialize_xml(child))
    return out

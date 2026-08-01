"""Generated from Smithy shape ``com.amazonaws.s3#AnalyticsConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.analytics_configuration

AnalyticsConfigurationList: TypeAlias = list[
    "capo_s3.types.analytics_configuration.AnalyticsConfiguration"
]


# --- restXml ser/de ---
def serialize_xml(value: AnalyticsConfigurationList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_s3.types.analytics_configuration

        capo_s3.types.analytics_configuration.serialize_xml(item, el, "member")


def deserialize_xml(el: Element) -> AnalyticsConfigurationList:
    import capo_s3.types.analytics_configuration

    out: AnalyticsConfigurationList = []
    for child in el.findall("member"):
        out.append(capo_s3.types.analytics_configuration.deserialize_xml(child))
    return out


def serialize_xml_flat(
    value: AnalyticsConfigurationList, parent: Element, tag: str
) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_s3.types.analytics_configuration

        capo_s3.types.analytics_configuration.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> AnalyticsConfigurationList:
    import capo_s3.types.analytics_configuration

    out: AnalyticsConfigurationList = []
    for child in parent.findall(tag):
        out.append(capo_s3.types.analytics_configuration.deserialize_xml(child))
    return out

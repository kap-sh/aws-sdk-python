"""Generated from Smithy shape ``com.amazonaws.cloudfront#RealtimeLogConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.realtime_log_config

RealtimeLogConfigList: TypeAlias = list[
    "capo_cloudfront.types.realtime_log_config.RealtimeLogConfig"
]


# --- restXml ser/de ---
def serialize_xml(value: RealtimeLogConfigList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_cloudfront.types.realtime_log_config

        capo_cloudfront.types.realtime_log_config.serialize_xml(item, el, "member")


def deserialize_xml(el: Element) -> RealtimeLogConfigList:
    import capo_cloudfront.types.realtime_log_config

    out: RealtimeLogConfigList = []
    for child in el.findall("member"):
        out.append(capo_cloudfront.types.realtime_log_config.deserialize_xml(child))
    return out


def serialize_xml_flat(value: RealtimeLogConfigList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import capo_cloudfront.types.realtime_log_config

        capo_cloudfront.types.realtime_log_config.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> RealtimeLogConfigList:
    import capo_cloudfront.types.realtime_log_config

    out: RealtimeLogConfigList = []
    for child in parent.findall(tag):
        out.append(capo_cloudfront.types.realtime_log_config.deserialize_xml(child))
    return out

"""Generated from Smithy shape ``com.amazonaws.route53#QueryLoggingConfigs``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.query_logging_config

QueryLoggingConfigs: TypeAlias = list[
    "capo_route_53.types.query_logging_config.QueryLoggingConfig"
]


# --- restXml ser/de ---
def serialize_xml(value: QueryLoggingConfigs, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_route_53.types.query_logging_config

        capo_route_53.types.query_logging_config.serialize_xml(
            item, el, "QueryLoggingConfig"
        )


def deserialize_xml(el: Element) -> QueryLoggingConfigs:
    import capo_route_53.types.query_logging_config

    out: QueryLoggingConfigs = []
    for child in el.findall("QueryLoggingConfig"):
        out.append(capo_route_53.types.query_logging_config.deserialize_xml(child))
    return out


def serialize_xml_flat(value: QueryLoggingConfigs, parent: Element, tag: str) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_route_53.types.query_logging_config

        capo_route_53.types.query_logging_config.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> QueryLoggingConfigs:
    import capo_route_53.types.query_logging_config

    out: QueryLoggingConfigs = []
    for child in parent.findall(tag):
        out.append(capo_route_53.types.query_logging_config.deserialize_xml(child))
    return out

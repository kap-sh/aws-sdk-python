"""Generated from Smithy shape ``com.amazonaws.route53#QueryLoggingConfigs``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.query_logging_config

QueryLoggingConfigs: TypeAlias = list[
    "aws_sdk_route_53.types.query_logging_config.QueryLoggingConfig"
]


# --- restXml ser/de ---
def serialize_xml(value: QueryLoggingConfigs, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_route_53.types.query_logging_config

        aws_sdk_route_53.types.query_logging_config.serialize_xml(
            item, el, "QueryLoggingConfig"
        )


def deserialize_xml(el: Element) -> QueryLoggingConfigs:
    import aws_sdk_route_53.types.query_logging_config

    out: QueryLoggingConfigs = []
    for child in el.findall("QueryLoggingConfig"):
        out.append(aws_sdk_route_53.types.query_logging_config.deserialize_xml(child))
    return out


def serialize_xml_flat(value: QueryLoggingConfigs, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_route_53.types.query_logging_config

        aws_sdk_route_53.types.query_logging_config.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> QueryLoggingConfigs:
    import aws_sdk_route_53.types.query_logging_config

    out: QueryLoggingConfigs = []
    for child in parent.findall(tag):
        out.append(aws_sdk_route_53.types.query_logging_config.deserialize_xml(child))
    return out

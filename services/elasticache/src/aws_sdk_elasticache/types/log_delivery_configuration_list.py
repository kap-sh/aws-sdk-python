"""Generated from Smithy shape ``com.amazonaws.elasticache#LogDeliveryConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.log_delivery_configuration

LogDeliveryConfigurationList: TypeAlias = list[
    "aws_sdk_elasticache.types.log_delivery_configuration.LogDeliveryConfiguration"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: LogDeliveryConfigurationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.log_delivery_configuration

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.log_delivery_configuration.serialize_query(
            item, pairs, f"{prefix}.LogDeliveryConfiguration.{n}"
        )


def deserialize_query(el: Element) -> LogDeliveryConfigurationList:
    import aws_sdk_elasticache.types.log_delivery_configuration

    out: LogDeliveryConfigurationList = []
    for child in el.findall("LogDeliveryConfiguration"):
        out.append(
            aws_sdk_elasticache.types.log_delivery_configuration.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: LogDeliveryConfigurationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.log_delivery_configuration

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.log_delivery_configuration.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> LogDeliveryConfigurationList:
    import aws_sdk_elasticache.types.log_delivery_configuration

    out: LogDeliveryConfigurationList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elasticache.types.log_delivery_configuration.deserialize_query(
                child
            )
        )
    return out

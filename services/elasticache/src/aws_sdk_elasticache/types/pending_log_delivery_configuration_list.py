"""Generated from Smithy shape ``com.amazonaws.elasticache#PendingLogDeliveryConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.pending_log_delivery_configuration

PendingLogDeliveryConfigurationList: TypeAlias = list[
    "aws_sdk_elasticache.types.pending_log_delivery_configuration.PendingLogDeliveryConfiguration"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: PendingLogDeliveryConfigurationList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import aws_sdk_elasticache.types.pending_log_delivery_configuration

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.pending_log_delivery_configuration.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> PendingLogDeliveryConfigurationList:
    import aws_sdk_elasticache.types.pending_log_delivery_configuration

    out: PendingLogDeliveryConfigurationList = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_elasticache.types.pending_log_delivery_configuration.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: PendingLogDeliveryConfigurationList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import aws_sdk_elasticache.types.pending_log_delivery_configuration

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.pending_log_delivery_configuration.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> PendingLogDeliveryConfigurationList:
    import aws_sdk_elasticache.types.pending_log_delivery_configuration

    out: PendingLogDeliveryConfigurationList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elasticache.types.pending_log_delivery_configuration.deserialize_query(
                child
            )
        )
    return out

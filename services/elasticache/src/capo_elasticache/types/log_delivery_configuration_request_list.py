"""Generated from Smithy shape ``com.amazonaws.elasticache#LogDeliveryConfigurationRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.log_delivery_configuration_request

LogDeliveryConfigurationRequestList: TypeAlias = list[
    "capo_elasticache.types.log_delivery_configuration_request.LogDeliveryConfigurationRequest"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: LogDeliveryConfigurationRequestList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import capo_elasticache.types.log_delivery_configuration_request

    for n, item in enumerate(value, 1):
        capo_elasticache.types.log_delivery_configuration_request.serialize_query(
            item, pairs, f"{prefix}.LogDeliveryConfigurationRequest.{n}"
        )


def deserialize_query(el: Element) -> LogDeliveryConfigurationRequestList:
    import capo_elasticache.types.log_delivery_configuration_request

    out: LogDeliveryConfigurationRequestList = []
    for child in el.findall("LogDeliveryConfigurationRequest"):
        out.append(
            capo_elasticache.types.log_delivery_configuration_request.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: LogDeliveryConfigurationRequestList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import capo_elasticache.types.log_delivery_configuration_request

    for n, item in enumerate(value, 1):
        capo_elasticache.types.log_delivery_configuration_request.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> LogDeliveryConfigurationRequestList:
    import capo_elasticache.types.log_delivery_configuration_request

    out: LogDeliveryConfigurationRequestList = []
    for child in parent.findall(tag):
        out.append(
            capo_elasticache.types.log_delivery_configuration_request.deserialize_query(
                child
            )
        )
    return out

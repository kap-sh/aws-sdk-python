"""Generated from Smithy shape ``com.amazonaws.batch#ServiceEnvironmentOrders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.service_environment_order

ServiceEnvironmentOrders: TypeAlias = list[
    "capo_batch.types.service_environment_order.ServiceEnvironmentOrder"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceEnvironmentOrders) -> list:
    import capo_batch.types.service_environment_order

    out: list = []
    for item in value:
        out.append(capo_batch.types.service_environment_order.serialize_json(item))
    return out


def deserialize_json(data: list) -> ServiceEnvironmentOrders:
    import capo_batch.types.service_environment_order

    out: ServiceEnvironmentOrders = []
    for item in data:
        out.append(capo_batch.types.service_environment_order.deserialize_json(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.batch#ServiceEnvironmentOrders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.service_environment_order

ServiceEnvironmentOrders: TypeAlias = list[
    "aws_sdk_batch.types.service_environment_order.ServiceEnvironmentOrder"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceEnvironmentOrders) -> list:
    import aws_sdk_batch.types.service_environment_order

    out: list = []
    for item in value:
        out.append(aws_sdk_batch.types.service_environment_order.serialize_json(item))
    return out


def deserialize_json(data: list) -> ServiceEnvironmentOrders:
    import aws_sdk_batch.types.service_environment_order

    out: ServiceEnvironmentOrders = []
    for item in data:
        out.append(aws_sdk_batch.types.service_environment_order.deserialize_json(item))
    return out

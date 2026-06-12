"""Generated from Smithy shape ``com.amazonaws.batch#ComputeEnvironmentOrders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.compute_environment_order

ComputeEnvironmentOrders: TypeAlias = list[
    "aws_sdk_batch.types.compute_environment_order.ComputeEnvironmentOrder"
]


# --- restJson1 ser/de ---
def serialize_json(value: ComputeEnvironmentOrders) -> list:
    import aws_sdk_batch.types.compute_environment_order

    out: list = []
    for item in value:
        out.append(aws_sdk_batch.types.compute_environment_order.serialize_json(item))
    return out


def deserialize_json(data: list) -> ComputeEnvironmentOrders:
    import aws_sdk_batch.types.compute_environment_order

    out: ComputeEnvironmentOrders = []
    for item in data:
        out.append(aws_sdk_batch.types.compute_environment_order.deserialize_json(item))
    return out

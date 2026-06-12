"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#Filters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.filter

Filters: TypeAlias = list["aws_sdk_compute_optimizer.types.filter.Filter"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Filters) -> list:
    import aws_sdk_compute_optimizer.types.filter

    out: list = []
    for item in value:
        out.append(aws_sdk_compute_optimizer.types.filter.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Filters:
    import aws_sdk_compute_optimizer.types.filter

    out: Filters = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.filter.deserialize_aws_json_1_0(item)
        )
    return out

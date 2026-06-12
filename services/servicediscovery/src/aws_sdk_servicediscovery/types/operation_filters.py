"""Generated from Smithy shape ``com.amazonaws.servicediscovery#OperationFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.operation_filter

OperationFilters: TypeAlias = list[
    "aws_sdk_servicediscovery.types.operation_filter.OperationFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OperationFilters) -> list:
    import aws_sdk_servicediscovery.types.operation_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_servicediscovery.types.operation_filter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OperationFilters:
    import aws_sdk_servicediscovery.types.operation_filter

    out: OperationFilters = []
    for item in data:
        out.append(
            aws_sdk_servicediscovery.types.operation_filter.deserialize_aws_json_1_1(
                item
            )
        )
    return out

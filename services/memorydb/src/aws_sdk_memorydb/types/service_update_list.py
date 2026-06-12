"""Generated from Smithy shape ``com.amazonaws.memorydb#ServiceUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.service_update

ServiceUpdateList: TypeAlias = list[
    "aws_sdk_memorydb.types.service_update.ServiceUpdate"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceUpdateList) -> list:
    import aws_sdk_memorydb.types.service_update

    out: list = []
    for item in value:
        out.append(aws_sdk_memorydb.types.service_update.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ServiceUpdateList:
    import aws_sdk_memorydb.types.service_update

    out: ServiceUpdateList = []
    for item in data:
        out.append(aws_sdk_memorydb.types.service_update.deserialize_aws_json_1_1(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.memorydb#ServiceUpdateStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.service_update_status

ServiceUpdateStatusList: TypeAlias = list[
    "aws_sdk_memorydb.types.service_update_status.ServiceUpdateStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceUpdateStatusList) -> list:
    import aws_sdk_memorydb.types.service_update_status

    out: list = []
    for item in value:
        out.append(
            aws_sdk_memorydb.types.service_update_status.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ServiceUpdateStatusList:
    import aws_sdk_memorydb.types.service_update_status

    out: ServiceUpdateStatusList = []
    for item in data:
        out.append(
            aws_sdk_memorydb.types.service_update_status.deserialize_aws_json_1_1(item)
        )
    return out

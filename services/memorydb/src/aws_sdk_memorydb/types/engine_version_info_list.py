"""Generated from Smithy shape ``com.amazonaws.memorydb#EngineVersionInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.engine_version_info

EngineVersionInfoList: TypeAlias = list[
    "aws_sdk_memorydb.types.engine_version_info.EngineVersionInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EngineVersionInfoList) -> list:
    import aws_sdk_memorydb.types.engine_version_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_memorydb.types.engine_version_info.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EngineVersionInfoList:
    import aws_sdk_memorydb.types.engine_version_info

    out: EngineVersionInfoList = []
    for item in data:
        out.append(
            aws_sdk_memorydb.types.engine_version_info.deserialize_aws_json_1_1(item)
        )
    return out

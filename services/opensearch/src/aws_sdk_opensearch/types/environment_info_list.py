"""Generated from Smithy shape ``com.amazonaws.opensearch#EnvironmentInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.environment_info

EnvironmentInfoList: TypeAlias = list[
    "aws_sdk_opensearch.types.environment_info.EnvironmentInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentInfoList) -> list:
    import aws_sdk_opensearch.types.environment_info

    out: list = []
    for item in value:
        out.append(aws_sdk_opensearch.types.environment_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> EnvironmentInfoList:
    import aws_sdk_opensearch.types.environment_info

    out: EnvironmentInfoList = []
    for item in data:
        out.append(aws_sdk_opensearch.types.environment_info.deserialize_json(item))
    return out

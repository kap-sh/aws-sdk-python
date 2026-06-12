"""Generated from Smithy shape ``com.amazonaws.gamelift#ServerProcessList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.server_process

ServerProcessList: TypeAlias = list[
    "aws_sdk_gamelift.types.server_process.ServerProcess"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServerProcessList) -> list:
    import aws_sdk_gamelift.types.server_process

    out: list = []
    for item in value:
        out.append(aws_sdk_gamelift.types.server_process.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ServerProcessList:
    import aws_sdk_gamelift.types.server_process

    out: ServerProcessList = []
    for item in data:
        out.append(aws_sdk_gamelift.types.server_process.deserialize_aws_json_1_1(item))
    return out

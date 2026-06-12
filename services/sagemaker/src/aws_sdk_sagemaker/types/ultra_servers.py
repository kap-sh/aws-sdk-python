"""Generated from Smithy shape ``com.amazonaws.sagemaker#UltraServers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.ultra_server

UltraServers: TypeAlias = list["aws_sdk_sagemaker.types.ultra_server.UltraServer"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UltraServers) -> list:
    import aws_sdk_sagemaker.types.ultra_server

    out: list = []
    for item in value:
        out.append(aws_sdk_sagemaker.types.ultra_server.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> UltraServers:
    import aws_sdk_sagemaker.types.ultra_server

    out: UltraServers = []
    for item in data:
        out.append(aws_sdk_sagemaker.types.ultra_server.deserialize_aws_json_1_1(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.sagemaker#UltraServers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.ultra_server

UltraServers: TypeAlias = list["capo_sagemaker.types.ultra_server.UltraServer"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UltraServers) -> list:
    import capo_sagemaker.types.ultra_server

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.ultra_server.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> UltraServers:
    import capo_sagemaker.types.ultra_server

    out: UltraServers = []
    for item in data:
        out.append(capo_sagemaker.types.ultra_server.deserialize_aws_json_1_1(item))
    return out

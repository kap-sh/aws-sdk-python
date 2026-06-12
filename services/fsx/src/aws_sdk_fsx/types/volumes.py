"""Generated from Smithy shape ``com.amazonaws.fsx#Volumes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fsx.types.volume

Volumes: TypeAlias = list["aws_sdk_fsx.types.volume.Volume"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Volumes) -> list:
    import aws_sdk_fsx.types.volume

    out: list = []
    for item in value:
        out.append(aws_sdk_fsx.types.volume.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Volumes:
    import aws_sdk_fsx.types.volume

    out: Volumes = []
    for item in data:
        out.append(aws_sdk_fsx.types.volume.deserialize_aws_json_1_1(item))
    return out

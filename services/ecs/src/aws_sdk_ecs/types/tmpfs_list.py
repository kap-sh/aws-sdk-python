"""Generated from Smithy shape ``com.amazonaws.ecs#TmpfsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.tmpfs

TmpfsList: TypeAlias = list["aws_sdk_ecs.types.tmpfs.Tmpfs"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TmpfsList) -> list:
    import aws_sdk_ecs.types.tmpfs

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.tmpfs.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TmpfsList:
    import aws_sdk_ecs.types.tmpfs

    out: TmpfsList = []
    for item in data:
        out.append(aws_sdk_ecs.types.tmpfs.deserialize_aws_json_1_1(item))
    return out

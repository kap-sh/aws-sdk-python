"""Generated from Smithy shape ``com.amazonaws.ecs#TmpfsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.tmpfs

TmpfsList: TypeAlias = list["capo_ecs.types.tmpfs.Tmpfs"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TmpfsList) -> list:
    import capo_ecs.types.tmpfs

    out: list = []
    for item in value:
        out.append(capo_ecs.types.tmpfs.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TmpfsList:
    import capo_ecs.types.tmpfs

    out: TmpfsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.tmpfs.deserialize_aws_json_1_1(item))
    return out

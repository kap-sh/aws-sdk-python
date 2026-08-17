"""Generated from Smithy shape ``com.amazonaws.ecs#UlimitList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.ulimit

UlimitList: TypeAlias = list["capo_ecs.types.ulimit.Ulimit"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UlimitList) -> list:
    import capo_ecs.types.ulimit

    out: list = []
    for item in value:
        out.append(capo_ecs.types.ulimit.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> UlimitList:
    import capo_ecs.types.ulimit

    out: UlimitList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.ulimit.deserialize_aws_json_1_1(item))
    return out

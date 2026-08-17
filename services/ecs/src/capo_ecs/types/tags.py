"""Generated from Smithy shape ``com.amazonaws.ecs#Tags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.tag

Tags: TypeAlias = list["capo_ecs.types.tag.Tag"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tags) -> list:
    import capo_ecs.types.tag

    out: list = []
    for item in value:
        out.append(capo_ecs.types.tag.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Tags:
    import capo_ecs.types.tag

    out: Tags = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.tag.deserialize_aws_json_1_1(item))
    return out

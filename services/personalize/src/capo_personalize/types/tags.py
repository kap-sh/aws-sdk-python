"""Generated from Smithy shape ``com.amazonaws.personalize#Tags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_personalize.types.tag

Tags: TypeAlias = list["capo_personalize.types.tag.Tag"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tags) -> list:
    import capo_personalize.types.tag

    out: list = []
    for item in value:
        out.append(capo_personalize.types.tag.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Tags:
    import capo_personalize.types.tag

    out: Tags = []
    for item in data:
        out.append(capo_personalize.types.tag.deserialize_aws_json_1_1(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.efs#Tags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_efs.types.tag

Tags: TypeAlias = list["aws_sdk_efs.types.tag.Tag"]


# --- restJson1 ser/de ---
def serialize_json(value: Tags) -> list:
    import aws_sdk_efs.types.tag

    out: list = []
    for item in value:
        out.append(aws_sdk_efs.types.tag.serialize_json(item))
    return out


def deserialize_json(data: list) -> Tags:
    import aws_sdk_efs.types.tag

    out: Tags = []
    for item in data:
        out.append(aws_sdk_efs.types.tag.deserialize_json(item))
    return out

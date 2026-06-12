"""Generated from Smithy shape ``com.amazonaws.pipes#PipeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pipes.types.pipe

PipeList: TypeAlias = list["aws_sdk_pipes.types.pipe.Pipe"]


# --- restJson1 ser/de ---
def serialize_json(value: PipeList) -> list:
    import aws_sdk_pipes.types.pipe

    out: list = []
    for item in value:
        out.append(aws_sdk_pipes.types.pipe.serialize_json(item))
    return out


def deserialize_json(data: list) -> PipeList:
    import aws_sdk_pipes.types.pipe

    out: PipeList = []
    for item in data:
        out.append(aws_sdk_pipes.types.pipe.deserialize_json(item))
    return out

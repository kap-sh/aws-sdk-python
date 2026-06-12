"""Generated from Smithy shape ``com.amazonaws.polly#SynthesisTasks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_polly.types.synthesis_task

SynthesisTasks: TypeAlias = list["aws_sdk_polly.types.synthesis_task.SynthesisTask"]


# --- restJson1 ser/de ---
def serialize_json(value: SynthesisTasks) -> list:
    import aws_sdk_polly.types.synthesis_task

    out: list = []
    for item in value:
        out.append(aws_sdk_polly.types.synthesis_task.serialize_json(item))
    return out


def deserialize_json(data: list) -> SynthesisTasks:
    import aws_sdk_polly.types.synthesis_task

    out: SynthesisTasks = []
    for item in data:
        out.append(aws_sdk_polly.types.synthesis_task.deserialize_json(item))
    return out

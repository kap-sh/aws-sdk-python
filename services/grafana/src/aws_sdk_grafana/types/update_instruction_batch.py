"""Generated from Smithy shape ``com.amazonaws.grafana#UpdateInstructionBatch``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_grafana.types.update_instruction

UpdateInstructionBatch: TypeAlias = list[
    "aws_sdk_grafana.types.update_instruction.UpdateInstruction"
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateInstructionBatch) -> list:
    import aws_sdk_grafana.types.update_instruction

    out: list = []
    for item in value:
        out.append(aws_sdk_grafana.types.update_instruction.serialize_json(item))
    return out


def deserialize_json(data: list) -> UpdateInstructionBatch:
    import aws_sdk_grafana.types.update_instruction

    out: UpdateInstructionBatch = []
    for item in data:
        out.append(aws_sdk_grafana.types.update_instruction.deserialize_json(item))
    return out

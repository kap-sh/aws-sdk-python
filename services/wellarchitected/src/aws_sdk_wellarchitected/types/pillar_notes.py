"""Generated from Smithy shape ``com.amazonaws.wellarchitected#PillarNotes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.notes
    import aws_sdk_wellarchitected.types.pillar_id

PillarNotes: TypeAlias = dict[
    "aws_sdk_wellarchitected.types.pillar_id.PillarId",
    "aws_sdk_wellarchitected.types.notes.Notes",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: PillarNotes) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> PillarNotes:
    out: PillarNotes = {}
    for key, value in data.items():
        out[key] = value
    return out

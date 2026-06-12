"""Generated from Smithy shape ``com.amazonaws.wellarchitected#WorkloadPillarPriorities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.pillar_id

WorkloadPillarPriorities: TypeAlias = list[
    "aws_sdk_wellarchitected.types.pillar_id.PillarId"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadPillarPriorities) -> list:
    return list(value)


def deserialize_json(data: list) -> WorkloadPillarPriorities:
    return list(data)

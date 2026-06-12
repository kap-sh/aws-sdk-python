"""Generated from Smithy shape ``com.amazonaws.wellarchitected#PillarDifferences``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.pillar_difference

PillarDifferences: TypeAlias = list[
    "aws_sdk_wellarchitected.types.pillar_difference.PillarDifference"
]


# --- restJson1 ser/de ---
def serialize_json(value: PillarDifferences) -> list:
    import aws_sdk_wellarchitected.types.pillar_difference

    out: list = []
    for item in value:
        out.append(aws_sdk_wellarchitected.types.pillar_difference.serialize_json(item))
    return out


def deserialize_json(data: list) -> PillarDifferences:
    import aws_sdk_wellarchitected.types.pillar_difference

    out: PillarDifferences = []
    for item in data:
        out.append(
            aws_sdk_wellarchitected.types.pillar_difference.deserialize_json(item)
        )
    return out

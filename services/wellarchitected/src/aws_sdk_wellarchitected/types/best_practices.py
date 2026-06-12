"""Generated from Smithy shape ``com.amazonaws.wellarchitected#BestPractices``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.best_practice

BestPractices: TypeAlias = list[
    "aws_sdk_wellarchitected.types.best_practice.BestPractice"
]


# --- restJson1 ser/de ---
def serialize_json(value: BestPractices) -> list:
    import aws_sdk_wellarchitected.types.best_practice

    out: list = []
    for item in value:
        out.append(aws_sdk_wellarchitected.types.best_practice.serialize_json(item))
    return out


def deserialize_json(data: list) -> BestPractices:
    import aws_sdk_wellarchitected.types.best_practice

    out: BestPractices = []
    for item in data:
        out.append(aws_sdk_wellarchitected.types.best_practice.deserialize_json(item))
    return out

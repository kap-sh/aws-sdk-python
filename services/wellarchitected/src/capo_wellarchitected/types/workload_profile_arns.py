"""Generated from Smithy shape ``com.amazonaws.wellarchitected#WorkloadProfileArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.profile_arn

WorkloadProfileArns: TypeAlias = list[
    "capo_wellarchitected.types.profile_arn.ProfileArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadProfileArns) -> list:
    return list(value)


def deserialize_json(data: list) -> WorkloadProfileArns:
    return list(data)

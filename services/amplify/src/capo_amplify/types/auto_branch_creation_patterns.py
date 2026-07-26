"""Generated from Smithy shape ``com.amazonaws.amplify#AutoBranchCreationPatterns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_amplify.types.auto_branch_creation_pattern

AutoBranchCreationPatterns: TypeAlias = list[
    "capo_amplify.types.auto_branch_creation_pattern.AutoBranchCreationPattern"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutoBranchCreationPatterns) -> list:
    return list(value)


def deserialize_json(data: list) -> AutoBranchCreationPatterns:
    return list(data)

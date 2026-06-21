"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#RepositoryAssociationState``."""

from typing import Literal, TypeAlias, cast

RepositoryAssociationState: TypeAlias = Literal[
    "Associated",
    "Associating",
    "Failed",
    "Disassociating",
    "Disassociated",
]


# --- restJson1 ser/de ---
def serialize_json(value: RepositoryAssociationState) -> str:
    return value


def deserialize_json(data: str) -> RepositoryAssociationState:
    return cast(RepositoryAssociationState, data)

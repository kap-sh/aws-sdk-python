"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#RepositoryAssociationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codeguru_reviewer.errors import DeserializationError

RepositoryAssociationState: TypeAlias = Literal[
    "Associated",
    "Associating",
    "Failed",
    "Disassociating",
    "Disassociated",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Associated",
        "Associating",
        "Failed",
        "Disassociating",
        "Disassociated",
    )
)


def serialize_json(value: RepositoryAssociationState) -> str:
    return value


def deserialize_json(data: str) -> RepositoryAssociationState:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RepositoryAssociationState value: {data!r}"
        )
    return cast(RepositoryAssociationState, data)

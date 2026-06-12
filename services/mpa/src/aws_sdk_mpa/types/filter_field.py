"""Generated from Smithy shape ``com.amazonaws.mpa#FilterField``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mpa.errors import DeserializationError

FilterField: TypeAlias = Literal[
    "ActionName",
    "ApprovalTeamName",
    "VotingTime",
    "Vote",
    "SessionStatus",
    "InitiationTime",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ActionName",
        "ApprovalTeamName",
        "VotingTime",
        "Vote",
        "SessionStatus",
        "InitiationTime",
    )
)


def serialize_json(value: FilterField) -> str:
    return value


def deserialize_json(data: str) -> FilterField:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FilterField value: {data!r}")
    return cast(FilterField, data)

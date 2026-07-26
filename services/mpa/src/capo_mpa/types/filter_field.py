"""Generated from Smithy shape ``com.amazonaws.mpa#FilterField``."""

from typing import Literal, TypeAlias, cast

FilterField: TypeAlias = Literal[
    "ActionName",
    "ApprovalTeamName",
    "VotingTime",
    "Vote",
    "SessionStatus",
    "InitiationTime",
]


# --- restJson1 ser/de ---
def serialize_json(value: FilterField) -> str:
    return value


def deserialize_json(data: str) -> FilterField:
    return cast(FilterField, data)

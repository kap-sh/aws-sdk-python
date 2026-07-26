"""Generated from Smithy shape ``com.amazonaws.bedrock#CommitmentDuration``."""

from typing import Literal, TypeAlias, cast

CommitmentDuration: TypeAlias = Literal[
    "OneMonth",
    "SixMonths",
]


# --- restJson1 ser/de ---
def serialize_json(value: CommitmentDuration) -> str:
    return value


def deserialize_json(data: str) -> CommitmentDuration:
    return cast(CommitmentDuration, data)

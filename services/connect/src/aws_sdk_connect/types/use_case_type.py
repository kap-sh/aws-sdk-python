"""Generated from Smithy shape ``com.amazonaws.connect#UseCaseType``."""

from typing import Literal, TypeAlias, cast

UseCaseType: TypeAlias = Literal[
    "RULES_EVALUATION",
    "CONNECT_CAMPAIGNS",
]


# --- restJson1 ser/de ---
def serialize_json(value: UseCaseType) -> str:
    return value


def deserialize_json(data: str) -> UseCaseType:
    return cast(UseCaseType, data)

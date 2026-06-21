"""Generated from Smithy shape ``com.amazonaws.opensearch#PrincipalType``."""

from typing import Literal, TypeAlias, cast

PrincipalType: TypeAlias = Literal[
    "AWS_ACCOUNT",
    "AWS_SERVICE",
]


# --- restJson1 ser/de ---
def serialize_json(value: PrincipalType) -> str:
    return value


def deserialize_json(data: str) -> PrincipalType:
    return cast(PrincipalType, data)

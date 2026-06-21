"""Generated from Smithy shape ``com.amazonaws.amplify#RepositoryCloneMethod``."""

from typing import Literal, TypeAlias, cast

RepositoryCloneMethod: TypeAlias = Literal[
    "SSH",
    "TOKEN",
    "SIGV4",
]


# --- restJson1 ser/de ---
def serialize_json(value: RepositoryCloneMethod) -> str:
    return value


def deserialize_json(data: str) -> RepositoryCloneMethod:
    return cast(RepositoryCloneMethod, data)

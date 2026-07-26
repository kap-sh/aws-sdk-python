"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#Type``."""

from typing import Literal, TypeAlias, cast

Type: TypeAlias = Literal[
    "PullRequest",
    "RepositoryAnalysis",
]


# --- restJson1 ser/de ---
def serialize_json(value: Type) -> str:
    return value


def deserialize_json(data: str) -> Type:
    return cast(Type, data)

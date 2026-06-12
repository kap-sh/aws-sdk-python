"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#Type``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codeguru_reviewer.errors import DeserializationError

Type: TypeAlias = Literal[
    "PullRequest",
    "RepositoryAnalysis",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PullRequest",
        "RepositoryAnalysis",
    )
)


def serialize_json(value: Type) -> str:
    return value


def deserialize_json(data: str) -> Type:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Type value: {data!r}")
    return cast(Type, data)

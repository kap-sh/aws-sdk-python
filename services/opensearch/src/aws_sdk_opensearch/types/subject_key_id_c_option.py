"""Generated from Smithy shape ``com.amazonaws.opensearch#SubjectKeyIdCOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

SubjectKeyIdCOption: TypeAlias = Literal[
    "UserName",
    "UserId",
    "Email",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UserName",
        "UserId",
        "Email",
    )
)


def serialize_json(value: SubjectKeyIdCOption) -> str:
    return value


def deserialize_json(data: str) -> SubjectKeyIdCOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SubjectKeyIdCOption value: {data!r}")
    return cast(SubjectKeyIdCOption, data)

"""Generated from Smithy shape ``com.amazonaws.deadline#JobTemplateType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

JobTemplateType: TypeAlias = Literal[
    "JSON",
    "YAML",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "JSON",
        "YAML",
    )
)


def serialize_json(value: JobTemplateType) -> str:
    return value


def deserialize_json(data: str) -> JobTemplateType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobTemplateType value: {data!r}")
    return cast(JobTemplateType, data)

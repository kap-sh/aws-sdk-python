"""Generated from Smithy shape ``com.amazonaws.emrcontainers#TemplateParameterDataType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr_containers.errors import DeserializationError

TemplateParameterDataType: TypeAlias = Literal[
    "NUMBER",
    "STRING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NUMBER",
        "STRING",
    )
)


def serialize_json(value: TemplateParameterDataType) -> str:
    return value


def deserialize_json(data: str) -> TemplateParameterDataType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TemplateParameterDataType value: {data!r}")
    return cast(TemplateParameterDataType, data)

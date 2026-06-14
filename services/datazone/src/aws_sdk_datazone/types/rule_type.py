"""Generated from Smithy shape ``com.amazonaws.datazone#RuleType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

RuleType: TypeAlias = Literal[
    "METADATA_FORM_ENFORCEMENT",
    "GLOSSARY_TERM_ENFORCEMENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "METADATA_FORM_ENFORCEMENT",
        "GLOSSARY_TERM_ENFORCEMENT",
    )
)


def serialize_json(value: RuleType) -> str:
    return value


def deserialize_json(data: str) -> RuleType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleType value: {data!r}")
    return cast(RuleType, data)

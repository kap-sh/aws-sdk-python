"""Generated from Smithy shape ``com.amazonaws.datazone#RuleType``."""

from typing import Literal, TypeAlias, cast

RuleType: TypeAlias = Literal[
    "METADATA_FORM_ENFORCEMENT",
    "GLOSSARY_TERM_ENFORCEMENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: RuleType) -> str:
    return value


def deserialize_json(data: str) -> RuleType:
    return cast(RuleType, data)

"""Generated from Smithy shape ``com.amazonaws.resiliencehub#TemplateFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

TemplateFormat: TypeAlias = Literal[
    "CfnYaml",
    "CfnJson",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CfnYaml",
        "CfnJson",
    )
)


def serialize_json(value: TemplateFormat) -> str:
    return value


def deserialize_json(data: str) -> TemplateFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TemplateFormat value: {data!r}")
    return cast(TemplateFormat, data)

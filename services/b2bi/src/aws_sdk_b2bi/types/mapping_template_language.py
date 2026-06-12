"""Generated from Smithy shape ``com.amazonaws.b2bi#MappingTemplateLanguage``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_b2bi.errors import DeserializationError

MappingTemplateLanguage: TypeAlias = Literal[
    "XSLT",
    "JSONATA",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "XSLT",
        "JSONATA",
    )
)


def serialize_aws_json_1_0(value: MappingTemplateLanguage) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MappingTemplateLanguage:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MappingTemplateLanguage value: {data!r}")
    return cast(MappingTemplateLanguage, data)

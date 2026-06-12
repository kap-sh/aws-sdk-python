"""Generated from Smithy shape ``com.amazonaws.b2bi#MappingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_b2bi.errors import DeserializationError

MappingType: TypeAlias = Literal[
    "JSONATA",
    "XSLT",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "JSONATA",
        "XSLT",
    )
)


def serialize_aws_json_1_0(value: MappingType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MappingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MappingType value: {data!r}")
    return cast(MappingType, data)

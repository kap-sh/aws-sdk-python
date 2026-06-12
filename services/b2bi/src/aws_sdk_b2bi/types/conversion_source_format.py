"""Generated from Smithy shape ``com.amazonaws.b2bi#ConversionSourceFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_b2bi.errors import DeserializationError

ConversionSourceFormat: TypeAlias = Literal[
    "JSON",
    "XML",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "JSON",
        "XML",
    )
)


def serialize_aws_json_1_0(value: ConversionSourceFormat) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ConversionSourceFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConversionSourceFormat value: {data!r}")
    return cast(ConversionSourceFormat, data)

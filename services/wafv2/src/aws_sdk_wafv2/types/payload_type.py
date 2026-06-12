"""Generated from Smithy shape ``com.amazonaws.wafv2#PayloadType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wafv2.errors import DeserializationError

PayloadType: TypeAlias = Literal[
    "JSON",
    "FORM_ENCODED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "JSON",
        "FORM_ENCODED",
    )
)


def serialize_aws_json_1_1(value: PayloadType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PayloadType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PayloadType value: {data!r}")
    return cast(PayloadType, data)

"""Generated from Smithy shape ``com.amazonaws.glue#UnnestSpec``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

UnnestSpec: TypeAlias = Literal[
    "TOPLEVEL",
    "FULL",
    "NOUNNEST",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TOPLEVEL",
        "FULL",
        "NOUNNEST",
    )
)


def serialize_aws_json_1_1(value: UnnestSpec) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UnnestSpec:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UnnestSpec value: {data!r}")
    return cast(UnnestSpec, data)

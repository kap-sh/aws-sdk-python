"""Generated from Smithy shape ``com.amazonaws.glue#ComputationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

ComputationType: TypeAlias = Literal[
    "FULL",
    "INCREMENTAL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FULL",
        "INCREMENTAL",
    )
)


def serialize_aws_json_1_1(value: ComputationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ComputationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComputationType value: {data!r}")
    return cast(ComputationType, data)

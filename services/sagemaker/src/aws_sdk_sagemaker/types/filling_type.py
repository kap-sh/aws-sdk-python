"""Generated from Smithy shape ``com.amazonaws.sagemaker#FillingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

FillingType: TypeAlias = Literal[
    "frontfill",
    "middlefill",
    "backfill",
    "futurefill",
    "frontfill_value",
    "middlefill_value",
    "backfill_value",
    "futurefill_value",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "frontfill",
        "middlefill",
        "backfill",
        "futurefill",
        "frontfill_value",
        "middlefill_value",
        "backfill_value",
        "futurefill_value",
    )
)


def serialize_aws_json_1_1(value: FillingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FillingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FillingType value: {data!r}")
    return cast(FillingType, data)

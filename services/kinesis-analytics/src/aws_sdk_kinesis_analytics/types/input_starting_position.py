"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#InputStartingPosition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_analytics.errors import DeserializationError

InputStartingPosition: TypeAlias = Literal[
    "NOW",
    "TRIM_HORIZON",
    "LAST_STOPPED_POINT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NOW",
        "TRIM_HORIZON",
        "LAST_STOPPED_POINT",
    )
)


def serialize_aws_json_1_1(value: InputStartingPosition) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InputStartingPosition:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputStartingPosition value: {data!r}")
    return cast(InputStartingPosition, data)

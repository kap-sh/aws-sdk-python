"""Generated from Smithy shape ``com.amazonaws.frauddetector#DataSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_frauddetector.errors import DeserializationError

DataSource: TypeAlias = Literal[
    "EVENT",
    "MODEL_SCORE",
    "EXTERNAL_MODEL_SCORE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EVENT",
        "MODEL_SCORE",
        "EXTERNAL_MODEL_SCORE",
    )
)


def serialize_aws_json_1_1(value: DataSource) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataSource:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataSource value: {data!r}")
    return cast(DataSource, data)

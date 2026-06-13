"""Generated from Smithy shape ``com.amazonaws.emr#ReconfigurationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr.errors import DeserializationError

ReconfigurationType: TypeAlias = Literal[
    "OVERWRITE",
    "MERGE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OVERWRITE",
        "MERGE",
    )
)


def serialize_aws_json_1_1(value: ReconfigurationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReconfigurationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReconfigurationType value: {data!r}")
    return cast(ReconfigurationType, data)

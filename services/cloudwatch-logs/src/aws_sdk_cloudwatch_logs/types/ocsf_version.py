"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#OCSFVersion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_logs.errors import DeserializationError

OCSFVersion: TypeAlias = Literal[
    "V1.1",
    "V1.5",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "V1.1",
        "V1.5",
    )
)


def serialize_aws_json_1_1(value: OCSFVersion) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OCSFVersion:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OCSFVersion value: {data!r}")
    return cast(OCSFVersion, data)

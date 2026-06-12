"""Generated from Smithy shape ``com.amazonaws.healthlake#NlpStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_healthlake.errors import DeserializationError

NlpStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "ENABLING",
    "DISABLING",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
        "ENABLING",
        "DISABLING",
    )
)


def serialize_aws_json_1_0(value: NlpStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> NlpStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NlpStatus value: {data!r}")
    return cast(NlpStatus, data)

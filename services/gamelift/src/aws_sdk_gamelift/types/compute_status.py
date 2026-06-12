"""Generated from Smithy shape ``com.amazonaws.gamelift#ComputeStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

ComputeStatus: TypeAlias = Literal[
    "PENDING",
    "ACTIVE",
    "TERMINATING",
    "IMPAIRED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "ACTIVE",
        "TERMINATING",
        "IMPAIRED",
    )
)


def serialize_aws_json_1_1(value: ComputeStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ComputeStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComputeStatus value: {data!r}")
    return cast(ComputeStatus, data)

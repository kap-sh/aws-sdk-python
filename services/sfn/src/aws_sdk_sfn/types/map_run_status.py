"""Generated from Smithy shape ``com.amazonaws.sfn#MapRunStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sfn.errors import DeserializationError

MapRunStatus: TypeAlias = Literal[
    "RUNNING",
    "SUCCEEDED",
    "FAILED",
    "ABORTED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
        "ABORTED",
    )
)


def serialize_aws_json_1_0(value: MapRunStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MapRunStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MapRunStatus value: {data!r}")
    return cast(MapRunStatus, data)

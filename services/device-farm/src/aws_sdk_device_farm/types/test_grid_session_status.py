"""Generated from Smithy shape ``com.amazonaws.devicefarm#TestGridSessionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_device_farm.errors import DeserializationError

TestGridSessionStatus: TypeAlias = Literal[
    "ACTIVE",
    "CLOSED",
    "ERRORED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "CLOSED",
        "ERRORED",
    )
)


def serialize_aws_json_1_1(value: TestGridSessionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TestGridSessionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TestGridSessionStatus value: {data!r}")
    return cast(TestGridSessionStatus, data)

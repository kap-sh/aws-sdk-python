"""Generated from Smithy shape ``com.amazonaws.codedeploy#StopStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codedeploy.errors import DeserializationError

StopStatus: TypeAlias = Literal[
    "Pending",
    "Succeeded",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pending",
        "Succeeded",
    )
)


def serialize_aws_json_1_1(value: StopStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StopStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StopStatus value: {data!r}")
    return cast(StopStatus, data)

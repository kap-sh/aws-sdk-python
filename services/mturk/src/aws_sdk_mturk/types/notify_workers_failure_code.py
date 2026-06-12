"""Generated from Smithy shape ``com.amazonaws.mturk#NotifyWorkersFailureCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mturk.errors import DeserializationError

NotifyWorkersFailureCode: TypeAlias = Literal[
    "SoftFailure",
    "HardFailure",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SoftFailure",
        "HardFailure",
    )
)


def serialize_aws_json_1_1(value: NotifyWorkersFailureCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NotifyWorkersFailureCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NotifyWorkersFailureCode value: {data!r}")
    return cast(NotifyWorkersFailureCode, data)

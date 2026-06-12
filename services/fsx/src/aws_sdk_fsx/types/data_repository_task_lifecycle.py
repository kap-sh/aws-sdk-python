"""Generated from Smithy shape ``com.amazonaws.fsx#DataRepositoryTaskLifecycle``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

DataRepositoryTaskLifecycle: TypeAlias = Literal[
    "PENDING",
    "EXECUTING",
    "FAILED",
    "SUCCEEDED",
    "CANCELED",
    "CANCELING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "EXECUTING",
        "FAILED",
        "SUCCEEDED",
        "CANCELED",
        "CANCELING",
    )
)


def serialize_aws_json_1_1(value: DataRepositoryTaskLifecycle) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataRepositoryTaskLifecycle:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DataRepositoryTaskLifecycle value: {data!r}"
        )
    return cast(DataRepositoryTaskLifecycle, data)

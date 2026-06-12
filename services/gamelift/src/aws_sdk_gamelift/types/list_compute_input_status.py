"""Generated from Smithy shape ``com.amazonaws.gamelift#ListComputeInputStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

ListComputeInputStatus: TypeAlias = Literal[
    "ACTIVE",
    "IMPAIRED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "IMPAIRED",
    )
)


def serialize_aws_json_1_1(value: ListComputeInputStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ListComputeInputStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ListComputeInputStatus value: {data!r}")
    return cast(ListComputeInputStatus, data)

"""Generated from Smithy shape ``com.amazonaws.ssoadmin#StatusValues``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sso_admin.errors import DeserializationError

StatusValues: TypeAlias = Literal[
    "IN_PROGRESS",
    "FAILED",
    "SUCCEEDED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "FAILED",
        "SUCCEEDED",
    )
)


def serialize_aws_json_1_1(value: StatusValues) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StatusValues:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StatusValues value: {data!r}")
    return cast(StatusValues, data)

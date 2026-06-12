"""Generated from Smithy shape ``com.amazonaws.codecommit#OverrideStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codecommit.errors import DeserializationError

OverrideStatus: TypeAlias = Literal[
    "OVERRIDE",
    "REVOKE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OVERRIDE",
        "REVOKE",
    )
)


def serialize_aws_json_1_1(value: OverrideStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OverrideStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OverrideStatus value: {data!r}")
    return cast(OverrideStatus, data)

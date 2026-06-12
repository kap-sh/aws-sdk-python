"""Generated from Smithy shape ``com.amazonaws.ssoadmin#InstanceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sso_admin.errors import DeserializationError

InstanceStatus: TypeAlias = Literal[
    "CREATE_IN_PROGRESS",
    "CREATE_FAILED",
    "DELETE_IN_PROGRESS",
    "ACTIVE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE_IN_PROGRESS",
        "CREATE_FAILED",
        "DELETE_IN_PROGRESS",
        "ACTIVE",
    )
)


def serialize_aws_json_1_1(value: InstanceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InstanceStatus value: {data!r}")
    return cast(InstanceStatus, data)

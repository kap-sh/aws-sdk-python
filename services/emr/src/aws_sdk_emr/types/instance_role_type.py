"""Generated from Smithy shape ``com.amazonaws.emr#InstanceRoleType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr.errors import DeserializationError

InstanceRoleType: TypeAlias = Literal[
    "MASTER",
    "CORE",
    "TASK",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MASTER",
        "CORE",
        "TASK",
    )
)


def serialize_aws_json_1_1(value: InstanceRoleType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceRoleType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InstanceRoleType value: {data!r}")
    return cast(InstanceRoleType, data)

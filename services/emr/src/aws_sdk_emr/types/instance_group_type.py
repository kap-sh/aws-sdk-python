"""Generated from Smithy shape ``com.amazonaws.emr#InstanceGroupType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr.errors import DeserializationError

InstanceGroupType: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: InstanceGroupType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceGroupType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InstanceGroupType value: {data!r}")
    return cast(InstanceGroupType, data)

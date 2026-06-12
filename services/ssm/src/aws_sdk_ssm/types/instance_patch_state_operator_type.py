"""Generated from Smithy shape ``com.amazonaws.ssm#InstancePatchStateOperatorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

InstancePatchStateOperatorType: TypeAlias = Literal[
    "Equal",
    "NotEqual",
    "LessThan",
    "GreaterThan",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Equal",
        "NotEqual",
        "LessThan",
        "GreaterThan",
    )
)


def serialize_aws_json_1_1(value: InstancePatchStateOperatorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstancePatchStateOperatorType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown InstancePatchStateOperatorType value: {data!r}"
        )
    return cast(InstancePatchStateOperatorType, data)

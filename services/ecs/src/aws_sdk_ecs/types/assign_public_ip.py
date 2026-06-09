"""Generated from Smithy shape ``com.amazonaws.ecs#AssignPublicIp``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

AssignPublicIp: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: AssignPublicIp) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AssignPublicIp:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssignPublicIp value: {data!r}")
    return cast(AssignPublicIp, data)

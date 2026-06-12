"""Generated from Smithy shape ``com.amazonaws.codedeploy#InstanceAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codedeploy.errors import DeserializationError

InstanceAction: TypeAlias = Literal[
    "TERMINATE",
    "KEEP_ALIVE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TERMINATE",
        "KEEP_ALIVE",
    )
)


def serialize_aws_json_1_1(value: InstanceAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InstanceAction value: {data!r}")
    return cast(InstanceAction, data)

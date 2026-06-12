"""Generated from Smithy shape ``com.amazonaws.ssm#NodeFilterOperatorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

NodeFilterOperatorType: TypeAlias = Literal[
    "Equal",
    "NotEqual",
    "BeginWith",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Equal",
        "NotEqual",
        "BeginWith",
    )
)


def serialize_aws_json_1_1(value: NodeFilterOperatorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NodeFilterOperatorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NodeFilterOperatorType value: {data!r}")
    return cast(NodeFilterOperatorType, data)

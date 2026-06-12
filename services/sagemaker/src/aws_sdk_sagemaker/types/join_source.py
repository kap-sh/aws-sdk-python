"""Generated from Smithy shape ``com.amazonaws.sagemaker#JoinSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

JoinSource: TypeAlias = Literal[
    "Input",
    "None",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Input",
        "None",
    )
)


def serialize_aws_json_1_1(value: JoinSource) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> JoinSource:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JoinSource value: {data!r}")
    return cast(JoinSource, data)

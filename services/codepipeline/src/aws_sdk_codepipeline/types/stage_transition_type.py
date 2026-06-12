"""Generated from Smithy shape ``com.amazonaws.codepipeline#StageTransitionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codepipeline.errors import DeserializationError

StageTransitionType: TypeAlias = Literal[
    "Inbound",
    "Outbound",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Inbound",
        "Outbound",
    )
)


def serialize_aws_json_1_1(value: StageTransitionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StageTransitionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StageTransitionType value: {data!r}")
    return cast(StageTransitionType, data)

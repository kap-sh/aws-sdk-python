"""Generated from Smithy shape ``com.amazonaws.emr#ScaleDownBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr.errors import DeserializationError

ScaleDownBehavior: TypeAlias = Literal[
    "TERMINATE_AT_INSTANCE_HOUR",
    "TERMINATE_AT_TASK_COMPLETION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TERMINATE_AT_INSTANCE_HOUR",
        "TERMINATE_AT_TASK_COMPLETION",
    )
)


def serialize_aws_json_1_1(value: ScaleDownBehavior) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScaleDownBehavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScaleDownBehavior value: {data!r}")
    return cast(ScaleDownBehavior, data)

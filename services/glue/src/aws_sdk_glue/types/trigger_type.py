"""Generated from Smithy shape ``com.amazonaws.glue#TriggerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

TriggerType: TypeAlias = Literal[
    "SCHEDULED",
    "CONDITIONAL",
    "ON_DEMAND",
    "EVENT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SCHEDULED",
        "CONDITIONAL",
        "ON_DEMAND",
        "EVENT",
    )
)


def serialize_aws_json_1_1(value: TriggerType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TriggerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TriggerType value: {data!r}")
    return cast(TriggerType, data)

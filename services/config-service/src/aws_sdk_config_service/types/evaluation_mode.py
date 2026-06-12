"""Generated from Smithy shape ``com.amazonaws.configservice#EvaluationMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_config_service.errors import DeserializationError

EvaluationMode: TypeAlias = Literal[
    "DETECTIVE",
    "PROACTIVE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DETECTIVE",
        "PROACTIVE",
    )
)


def serialize_aws_json_1_1(value: EvaluationMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EvaluationMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EvaluationMode value: {data!r}")
    return cast(EvaluationMode, data)

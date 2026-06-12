"""Generated from Smithy shape ``com.amazonaws.configservice#RuleEvaluationVisibility``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_config_service.errors import DeserializationError

RuleEvaluationVisibility: TypeAlias = Literal[
    "EXTERNAL",
    "INTERNAL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EXTERNAL",
        "INTERNAL",
    )
)


def serialize_aws_json_1_1(value: RuleEvaluationVisibility) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RuleEvaluationVisibility:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleEvaluationVisibility value: {data!r}")
    return cast(RuleEvaluationVisibility, data)

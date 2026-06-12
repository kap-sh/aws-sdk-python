"""Generated from Smithy shape ``com.amazonaws.glue#DQCompositeRuleEvaluationMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

DQCompositeRuleEvaluationMethod: TypeAlias = Literal[
    "COLUMN",
    "ROW",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COLUMN",
        "ROW",
    )
)


def serialize_aws_json_1_1(value: DQCompositeRuleEvaluationMethod) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DQCompositeRuleEvaluationMethod:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DQCompositeRuleEvaluationMethod value: {data!r}"
        )
    return cast(DQCompositeRuleEvaluationMethod, data)

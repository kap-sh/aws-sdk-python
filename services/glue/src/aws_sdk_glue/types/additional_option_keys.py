"""Generated from Smithy shape ``com.amazonaws.glue#AdditionalOptionKeys``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

AdditionalOptionKeys: TypeAlias = Literal[
    "performanceTuning.caching",
    "observations.scope",
    "compositeRuleEvaluation.method",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "performanceTuning.caching",
        "observations.scope",
        "compositeRuleEvaluation.method",
    )
)


def serialize_aws_json_1_1(value: AdditionalOptionKeys) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AdditionalOptionKeys:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AdditionalOptionKeys value: {data!r}")
    return cast(AdditionalOptionKeys, data)

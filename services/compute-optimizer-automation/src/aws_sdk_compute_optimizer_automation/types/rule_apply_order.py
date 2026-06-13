"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#RuleApplyOrder``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer_automation.errors import DeserializationError

RuleApplyOrder: TypeAlias = Literal[
    "BeforeAccountRules",
    "AfterAccountRules",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BeforeAccountRules",
        "AfterAccountRules",
    )
)


def serialize_aws_json_1_0(value: RuleApplyOrder) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleApplyOrder:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleApplyOrder value: {data!r}")
    return cast(RuleApplyOrder, data)

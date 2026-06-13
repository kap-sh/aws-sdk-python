"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#RuleType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer_automation.errors import DeserializationError

RuleType: TypeAlias = Literal[
    "OrganizationRule",
    "AccountRule",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OrganizationRule",
        "AccountRule",
    )
)


def serialize_aws_json_1_0(value: RuleType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleType value: {data!r}")
    return cast(RuleType, data)

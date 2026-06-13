"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#RuleStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer_automation.errors import DeserializationError

RuleStatus: TypeAlias = Literal[
    "Active",
    "Inactive",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Active",
        "Inactive",
    )
)


def serialize_aws_json_1_0(value: RuleStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleStatus value: {data!r}")
    return cast(RuleStatus, data)

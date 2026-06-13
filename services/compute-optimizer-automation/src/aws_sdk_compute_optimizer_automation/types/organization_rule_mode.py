"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#OrganizationRuleMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer_automation.errors import DeserializationError

OrganizationRuleMode: TypeAlias = Literal[
    "AnyAllowed",
    "NoneAllowed",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AnyAllowed",
        "NoneAllowed",
    )
)


def serialize_aws_json_1_0(value: OrganizationRuleMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> OrganizationRuleMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OrganizationRuleMode value: {data!r}")
    return cast(OrganizationRuleMode, data)

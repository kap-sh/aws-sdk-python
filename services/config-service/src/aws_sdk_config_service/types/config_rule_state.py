"""Generated from Smithy shape ``com.amazonaws.configservice#ConfigRuleState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_config_service.errors import DeserializationError

ConfigRuleState: TypeAlias = Literal[
    "ACTIVE",
    "DELETING",
    "DELETING_RESULTS",
    "EVALUATING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "DELETING",
        "DELETING_RESULTS",
        "EVALUATING",
    )
)


def serialize_aws_json_1_1(value: ConfigRuleState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConfigRuleState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConfigRuleState value: {data!r}")
    return cast(ConfigRuleState, data)

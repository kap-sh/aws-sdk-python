"""Generated from Smithy shape ``com.amazonaws.budgets#ActionSubType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_budgets.errors import DeserializationError

ActionSubType: TypeAlias = Literal[
    "STOP_EC2_INSTANCES",
    "STOP_RDS_INSTANCES",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STOP_EC2_INSTANCES",
        "STOP_RDS_INSTANCES",
    )
)


def serialize_aws_json_1_1(value: ActionSubType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ActionSubType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActionSubType value: {data!r}")
    return cast(ActionSubType, data)

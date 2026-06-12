"""Generated from Smithy shape ``com.amazonaws.budgets#ActionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_budgets.errors import DeserializationError

ActionType: TypeAlias = Literal[
    "APPLY_IAM_POLICY",
    "APPLY_SCP_POLICY",
    "RUN_SSM_DOCUMENTS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "APPLY_IAM_POLICY",
        "APPLY_SCP_POLICY",
        "RUN_SSM_DOCUMENTS",
    )
)


def serialize_aws_json_1_1(value: ActionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ActionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActionType value: {data!r}")
    return cast(ActionType, data)

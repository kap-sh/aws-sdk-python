"""Generated from Smithy shape ``com.amazonaws.budgets#ApprovalModel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_budgets.errors import DeserializationError

ApprovalModel: TypeAlias = Literal[
    "AUTOMATIC",
    "MANUAL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTOMATIC",
        "MANUAL",
    )
)


def serialize_aws_json_1_1(value: ApprovalModel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ApprovalModel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApprovalModel value: {data!r}")
    return cast(ApprovalModel, data)

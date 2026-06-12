"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelApprovalStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ModelApprovalStatus: TypeAlias = Literal[
    "Approved",
    "Rejected",
    "PendingManualApproval",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Approved",
        "Rejected",
        "PendingManualApproval",
    )
)


def serialize_aws_json_1_1(value: ModelApprovalStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelApprovalStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelApprovalStatus value: {data!r}")
    return cast(ModelApprovalStatus, data)

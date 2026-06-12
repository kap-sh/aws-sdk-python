"""Generated from Smithy shape ``com.amazonaws.codepipeline#ApprovalStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codepipeline.errors import DeserializationError

ApprovalStatus: TypeAlias = Literal[
    "Approved",
    "Rejected",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Approved",
        "Rejected",
    )
)


def serialize_aws_json_1_1(value: ApprovalStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ApprovalStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApprovalStatus value: {data!r}")
    return cast(ApprovalStatus, data)

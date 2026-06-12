"""Generated from Smithy shape ``com.amazonaws.codecommit#ApprovalState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codecommit.errors import DeserializationError

ApprovalState: TypeAlias = Literal[
    "APPROVE",
    "REVOKE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "APPROVE",
        "REVOKE",
    )
)


def serialize_aws_json_1_1(value: ApprovalState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ApprovalState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApprovalState value: {data!r}")
    return cast(ApprovalState, data)

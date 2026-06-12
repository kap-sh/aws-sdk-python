"""Generated from Smithy shape ``com.amazonaws.ecr#LifecyclePolicyPreviewStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecr.errors import DeserializationError

LifecyclePolicyPreviewStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETE",
    "EXPIRED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "COMPLETE",
        "EXPIRED",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: LifecyclePolicyPreviewStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LifecyclePolicyPreviewStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown LifecyclePolicyPreviewStatus value: {data!r}"
        )
    return cast(LifecyclePolicyPreviewStatus, data)

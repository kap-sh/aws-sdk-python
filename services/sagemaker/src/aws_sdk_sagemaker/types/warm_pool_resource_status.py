"""Generated from Smithy shape ``com.amazonaws.sagemaker#WarmPoolResourceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

WarmPoolResourceStatus: TypeAlias = Literal[
    "Available",
    "Terminated",
    "Reused",
    "InUse",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Available",
        "Terminated",
        "Reused",
        "InUse",
    )
)


def serialize_aws_json_1_1(value: WarmPoolResourceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WarmPoolResourceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WarmPoolResourceStatus value: {data!r}")
    return cast(WarmPoolResourceStatus, data)

"""Generated from Smithy shape ``com.amazonaws.sagemaker#HubContentSupportStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

HubContentSupportStatus: TypeAlias = Literal[
    "Supported",
    "Deprecated",
    "Restricted",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Supported",
        "Deprecated",
        "Restricted",
    )
)


def serialize_aws_json_1_1(value: HubContentSupportStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HubContentSupportStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HubContentSupportStatus value: {data!r}")
    return cast(HubContentSupportStatus, data)

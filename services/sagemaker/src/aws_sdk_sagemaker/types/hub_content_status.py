"""Generated from Smithy shape ``com.amazonaws.sagemaker#HubContentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

HubContentStatus: TypeAlias = Literal[
    "Available",
    "Importing",
    "Deleting",
    "ImportFailed",
    "DeleteFailed",
    "PendingImport",
    "PendingDelete",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Available",
        "Importing",
        "Deleting",
        "ImportFailed",
        "DeleteFailed",
        "PendingImport",
        "PendingDelete",
    )
)


def serialize_aws_json_1_1(value: HubContentStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HubContentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HubContentStatus value: {data!r}")
    return cast(HubContentStatus, data)

"""Generated from Smithy shape ``com.amazonaws.sagemaker#HubStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

HubStatus: TypeAlias = Literal[
    "InService",
    "Creating",
    "Updating",
    "Deleting",
    "CreateFailed",
    "UpdateFailed",
    "DeleteFailed",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InService",
        "Creating",
        "Updating",
        "Deleting",
        "CreateFailed",
        "UpdateFailed",
        "DeleteFailed",
    )
)


def serialize_aws_json_1_1(value: HubStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HubStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HubStatus value: {data!r}")
    return cast(HubStatus, data)

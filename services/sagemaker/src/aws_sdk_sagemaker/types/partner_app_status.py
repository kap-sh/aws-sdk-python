"""Generated from Smithy shape ``com.amazonaws.sagemaker#PartnerAppStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

PartnerAppStatus: TypeAlias = Literal[
    "Creating",
    "Updating",
    "Deleting",
    "Available",
    "Failed",
    "UpdateFailed",
    "Deleted",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Creating",
        "Updating",
        "Deleting",
        "Available",
        "Failed",
        "UpdateFailed",
        "Deleted",
    )
)


def serialize_aws_json_1_1(value: PartnerAppStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PartnerAppStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PartnerAppStatus value: {data!r}")
    return cast(PartnerAppStatus, data)

"""Generated from Smithy shape ``com.amazonaws.directoryservice#TrustState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service.errors import DeserializationError

TrustState: TypeAlias = Literal[
    "Creating",
    "Created",
    "Verifying",
    "VerifyFailed",
    "Verified",
    "Updating",
    "UpdateFailed",
    "Updated",
    "Deleting",
    "Deleted",
    "Failed",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Creating",
        "Created",
        "Verifying",
        "VerifyFailed",
        "Verified",
        "Updating",
        "UpdateFailed",
        "Updated",
        "Deleting",
        "Deleted",
        "Failed",
    )
)


def serialize_aws_json_1_1(value: TrustState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrustState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TrustState value: {data!r}")
    return cast(TrustState, data)

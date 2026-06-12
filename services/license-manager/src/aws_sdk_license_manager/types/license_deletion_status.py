"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseDeletionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_license_manager.errors import DeserializationError

LicenseDeletionStatus: TypeAlias = Literal[
    "PENDING_DELETE",
    "DELETED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING_DELETE",
        "DELETED",
    )
)


def serialize_aws_json_1_1(value: LicenseDeletionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LicenseDeletionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LicenseDeletionStatus value: {data!r}")
    return cast(LicenseDeletionStatus, data)

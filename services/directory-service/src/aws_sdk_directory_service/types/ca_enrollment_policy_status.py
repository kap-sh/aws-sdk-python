"""Generated from Smithy shape ``com.amazonaws.directoryservice#CaEnrollmentPolicyStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service.errors import DeserializationError

CaEnrollmentPolicyStatus: TypeAlias = Literal[
    "InProgress",
    "Success",
    "Failed",
    "Disabling",
    "Disabled",
    "Impaired",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InProgress",
        "Success",
        "Failed",
        "Disabling",
        "Disabled",
        "Impaired",
    )
)


def serialize_aws_json_1_1(value: CaEnrollmentPolicyStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CaEnrollmentPolicyStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CaEnrollmentPolicyStatus value: {data!r}")
    return cast(CaEnrollmentPolicyStatus, data)

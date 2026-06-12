"""Generated from Smithy shape ``com.amazonaws.ssm#PatchComplianceDataState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

PatchComplianceDataState: TypeAlias = Literal[
    "INSTALLED",
    "INSTALLED_OTHER",
    "INSTALLED_PENDING_REBOOT",
    "INSTALLED_REJECTED",
    "MISSING",
    "NOT_APPLICABLE",
    "FAILED",
    "AVAILABLE_SECURITY_UPDATE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INSTALLED",
        "INSTALLED_OTHER",
        "INSTALLED_PENDING_REBOOT",
        "INSTALLED_REJECTED",
        "MISSING",
        "NOT_APPLICABLE",
        "FAILED",
        "AVAILABLE_SECURITY_UPDATE",
    )
)


def serialize_aws_json_1_1(value: PatchComplianceDataState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PatchComplianceDataState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PatchComplianceDataState value: {data!r}")
    return cast(PatchComplianceDataState, data)

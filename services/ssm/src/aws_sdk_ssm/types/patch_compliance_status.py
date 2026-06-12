"""Generated from Smithy shape ``com.amazonaws.ssm#PatchComplianceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

PatchComplianceStatus: TypeAlias = Literal[
    "COMPLIANT",
    "NON_COMPLIANT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPLIANT",
        "NON_COMPLIANT",
    )
)


def serialize_aws_json_1_1(value: PatchComplianceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PatchComplianceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PatchComplianceStatus value: {data!r}")
    return cast(PatchComplianceStatus, data)

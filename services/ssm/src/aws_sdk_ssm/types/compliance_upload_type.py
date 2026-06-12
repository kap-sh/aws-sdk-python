"""Generated from Smithy shape ``com.amazonaws.ssm#ComplianceUploadType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

ComplianceUploadType: TypeAlias = Literal[
    "COMPLETE",
    "PARTIAL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPLETE",
        "PARTIAL",
    )
)


def serialize_aws_json_1_1(value: ComplianceUploadType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ComplianceUploadType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComplianceUploadType value: {data!r}")
    return cast(ComplianceUploadType, data)

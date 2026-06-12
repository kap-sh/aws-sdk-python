"""Generated from Smithy shape ``com.amazonaws.ssm#ComplianceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

ComplianceStatus: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: ComplianceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ComplianceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComplianceStatus value: {data!r}")
    return cast(ComplianceStatus, data)

"""Generated from Smithy shape ``com.amazonaws.configservice#ComplianceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_config_service.errors import DeserializationError

ComplianceType: TypeAlias = Literal[
    "COMPLIANT",
    "NON_COMPLIANT",
    "NOT_APPLICABLE",
    "INSUFFICIENT_DATA",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPLIANT",
        "NON_COMPLIANT",
        "NOT_APPLICABLE",
        "INSUFFICIENT_DATA",
    )
)


def serialize_aws_json_1_1(value: ComplianceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ComplianceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComplianceType value: {data!r}")
    return cast(ComplianceType, data)

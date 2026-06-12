"""Generated from Smithy shape ``com.amazonaws.configservice#ConformancePackComplianceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_config_service.errors import DeserializationError

ConformancePackComplianceType: TypeAlias = Literal[
    "COMPLIANT",
    "NON_COMPLIANT",
    "INSUFFICIENT_DATA",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPLIANT",
        "NON_COMPLIANT",
        "INSUFFICIENT_DATA",
    )
)


def serialize_aws_json_1_1(value: ConformancePackComplianceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConformancePackComplianceType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ConformancePackComplianceType value: {data!r}"
        )
    return cast(ConformancePackComplianceType, data)

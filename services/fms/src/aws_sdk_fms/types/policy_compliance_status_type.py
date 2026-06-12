"""Generated from Smithy shape ``com.amazonaws.fms#PolicyComplianceStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fms.errors import DeserializationError

PolicyComplianceStatusType: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: PolicyComplianceStatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PolicyComplianceStatusType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown PolicyComplianceStatusType value: {data!r}"
        )
    return cast(PolicyComplianceStatusType, data)

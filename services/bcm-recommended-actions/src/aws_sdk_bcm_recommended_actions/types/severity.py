"""Generated from Smithy shape ``com.amazonaws.bcmrecommendedactions#Severity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bcm_recommended_actions.errors import DeserializationError

Severity: TypeAlias = Literal[
    "INFO",
    "WARNING",
    "CRITICAL",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INFO",
        "WARNING",
        "CRITICAL",
    )
)


def serialize_aws_json_1_0(value: Severity) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Severity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Severity value: {data!r}")
    return cast(Severity, data)

"""Generated from Smithy shape ``com.amazonaws.bcmrecommendedactions#Severity``."""

from typing import Literal, TypeAlias, cast

Severity: TypeAlias = Literal[
    "INFO",
    "WARNING",
    "CRITICAL",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Severity) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Severity:
    return cast(Severity, data)

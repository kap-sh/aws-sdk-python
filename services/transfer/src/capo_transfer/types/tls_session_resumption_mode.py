"""Generated from Smithy shape ``com.amazonaws.transfer#TlsSessionResumptionMode``."""

from typing import Literal, TypeAlias, cast

TlsSessionResumptionMode: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
    "ENFORCED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TlsSessionResumptionMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TlsSessionResumptionMode:
    return cast(TlsSessionResumptionMode, data)

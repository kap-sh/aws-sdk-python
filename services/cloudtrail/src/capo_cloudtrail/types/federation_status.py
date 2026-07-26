"""Generated from Smithy shape ``com.amazonaws.cloudtrail#FederationStatus``."""

from typing import Literal, TypeAlias, cast

FederationStatus: TypeAlias = Literal[
    "ENABLING",
    "ENABLED",
    "DISABLING",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FederationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FederationStatus:
    return cast(FederationStatus, data)

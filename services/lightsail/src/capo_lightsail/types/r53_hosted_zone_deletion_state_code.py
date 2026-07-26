"""Generated from Smithy shape ``com.amazonaws.lightsail#R53HostedZoneDeletionStateCode``."""

from typing import Literal, TypeAlias, cast

R53HostedZoneDeletionStateCode: TypeAlias = Literal[
    "SUCCEEDED",
    "PENDING",
    "FAILED",
    "STARTED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: R53HostedZoneDeletionStateCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> R53HostedZoneDeletionStateCode:
    return cast(R53HostedZoneDeletionStateCode, data)

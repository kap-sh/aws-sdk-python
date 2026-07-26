"""Generated from Smithy shape ``com.amazonaws.lightsail#RenewalStatus``."""

from typing import Literal, TypeAlias, cast

RenewalStatus: TypeAlias = Literal[
    "PendingAutoRenewal",
    "PendingValidation",
    "Success",
    "Failed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RenewalStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RenewalStatus:
    return cast(RenewalStatus, data)

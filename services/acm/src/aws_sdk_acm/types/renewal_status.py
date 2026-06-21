"""Generated from Smithy shape ``com.amazonaws.acm#RenewalStatus``."""

from typing import Literal, TypeAlias, cast

RenewalStatus: TypeAlias = Literal[
    "PENDING_AUTO_RENEWAL",
    "PENDING_VALIDATION",
    "SUCCESS",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RenewalStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RenewalStatus:
    return cast(RenewalStatus, data)

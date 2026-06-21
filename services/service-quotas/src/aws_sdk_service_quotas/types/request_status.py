"""Generated from Smithy shape ``com.amazonaws.servicequotas#RequestStatus``."""

from typing import Literal, TypeAlias, cast

RequestStatus: TypeAlias = Literal[
    "PENDING",
    "CASE_OPENED",
    "APPROVED",
    "DENIED",
    "CASE_CLOSED",
    "NOT_APPROVED",
    "INVALID_REQUEST",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RequestStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RequestStatus:
    return cast(RequestStatus, data)

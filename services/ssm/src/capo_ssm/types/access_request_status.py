"""Generated from Smithy shape ``com.amazonaws.ssm#AccessRequestStatus``."""

from typing import Literal, TypeAlias, cast

AccessRequestStatus: TypeAlias = Literal[
    "Approved",
    "Rejected",
    "Revoked",
    "Expired",
    "Pending",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessRequestStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccessRequestStatus:
    return cast(AccessRequestStatus, data)

"""Generated from Smithy shape ``com.amazonaws.acm#DomainStatus``."""

from typing import Literal, TypeAlias, cast

DomainStatus: TypeAlias = Literal[
    "PENDING_VALIDATION",
    "SUCCESS",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DomainStatus:
    return cast(DomainStatus, data)

"""Generated from Smithy shape ``com.amazonaws.organizations#PolicyTypeStatus``."""

from typing import Literal, TypeAlias, cast

PolicyTypeStatus: TypeAlias = Literal[
    "ENABLED",
    "PENDING_ENABLE",
    "PENDING_DISABLE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PolicyTypeStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PolicyTypeStatus:
    return cast(PolicyTypeStatus, data)

"""Generated from Smithy shape ``com.amazonaws.transfer#SecurityPolicyResourceType``."""

from typing import Literal, TypeAlias, cast

SecurityPolicyResourceType: TypeAlias = Literal[
    "SERVER",
    "CONNECTOR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecurityPolicyResourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SecurityPolicyResourceType:
    return cast(SecurityPolicyResourceType, data)

"""Generated from Smithy shape ``com.amazonaws.lightsail#ContactMethodStatus``."""

from typing import Literal, TypeAlias, cast

ContactMethodStatus: TypeAlias = Literal[
    "PendingVerification",
    "Valid",
    "Invalid",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContactMethodStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContactMethodStatus:
    return cast(ContactMethodStatus, data)

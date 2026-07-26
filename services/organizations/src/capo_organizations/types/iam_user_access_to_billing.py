"""Generated from Smithy shape ``com.amazonaws.organizations#IAMUserAccessToBilling``."""

from typing import Literal, TypeAlias, cast

IAMUserAccessToBilling: TypeAlias = Literal[
    "ALLOW",
    "DENY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IAMUserAccessToBilling) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IAMUserAccessToBilling:
    return cast(IAMUserAccessToBilling, data)

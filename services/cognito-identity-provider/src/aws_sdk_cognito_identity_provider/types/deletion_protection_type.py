"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DeletionProtectionType``."""

from typing import Literal, TypeAlias, cast

DeletionProtectionType: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletionProtectionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeletionProtectionType:
    return cast(DeletionProtectionType, data)

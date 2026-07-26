"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#RecoveryOptionNameType``."""

from typing import Literal, TypeAlias, cast

RecoveryOptionNameType: TypeAlias = Literal[
    "verified_email",
    "verified_phone_number",
    "admin_only",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecoveryOptionNameType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecoveryOptionNameType:
    return cast(RecoveryOptionNameType, data)

"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#VerifiedAttributeType``."""

from typing import Literal, TypeAlias, cast

VerifiedAttributeType: TypeAlias = Literal[
    "phone_number",
    "email",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VerifiedAttributeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> VerifiedAttributeType:
    return cast(VerifiedAttributeType, data)

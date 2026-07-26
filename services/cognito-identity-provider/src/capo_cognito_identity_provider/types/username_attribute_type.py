"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UsernameAttributeType``."""

from typing import Literal, TypeAlias, cast

UsernameAttributeType: TypeAlias = Literal[
    "phone_number",
    "email",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UsernameAttributeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UsernameAttributeType:
    return cast(UsernameAttributeType, data)

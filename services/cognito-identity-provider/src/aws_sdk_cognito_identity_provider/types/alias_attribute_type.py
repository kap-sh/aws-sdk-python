"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AliasAttributeType``."""

from typing import Literal, TypeAlias, cast

AliasAttributeType: TypeAlias = Literal[
    "phone_number",
    "email",
    "preferred_username",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AliasAttributeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AliasAttributeType:
    return cast(AliasAttributeType, data)

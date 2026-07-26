"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UserVerificationType``."""

from typing import Literal, TypeAlias, cast

UserVerificationType: TypeAlias = Literal[
    "required",
    "preferred",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserVerificationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UserVerificationType:
    return cast(UserVerificationType, data)

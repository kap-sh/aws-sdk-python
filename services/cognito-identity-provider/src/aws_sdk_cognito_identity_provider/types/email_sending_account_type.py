"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#EmailSendingAccountType``."""

from typing import Literal, TypeAlias, cast

EmailSendingAccountType: TypeAlias = Literal[
    "COGNITO_DEFAULT",
    "DEVELOPER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EmailSendingAccountType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EmailSendingAccountType:
    return cast(EmailSendingAccountType, data)

"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#VerifySoftwareTokenResponseType``."""

from typing import Literal, TypeAlias, cast

VerifySoftwareTokenResponseType: TypeAlias = Literal[
    "SUCCESS",
    "ERROR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VerifySoftwareTokenResponseType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> VerifySoftwareTokenResponseType:
    return cast(VerifySoftwareTokenResponseType, data)

"""Generated from Smithy shape ``com.amazonaws.ssoadmin#AuthenticationMethodType``."""

from typing import Literal, TypeAlias, cast

AuthenticationMethodType: TypeAlias = Literal["IAM",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthenticationMethodType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AuthenticationMethodType:
    return cast(AuthenticationMethodType, data)

"""Generated from Smithy shape ``com.amazonaws.transfer#SftpAuthenticationMethods``."""

from typing import Literal, TypeAlias, cast

SftpAuthenticationMethods: TypeAlias = Literal[
    "PASSWORD",
    "PUBLIC_KEY",
    "PUBLIC_KEY_OR_PASSWORD",
    "PUBLIC_KEY_AND_PASSWORD",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SftpAuthenticationMethods) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SftpAuthenticationMethods:
    return cast(SftpAuthenticationMethods, data)

"""Generated from Smithy shape ``com.amazonaws.licensemanager#TokenType``."""

from typing import Literal, TypeAlias, cast

TokenType: TypeAlias = Literal["REFRESH_TOKEN",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TokenType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TokenType:
    return cast(TokenType, data)

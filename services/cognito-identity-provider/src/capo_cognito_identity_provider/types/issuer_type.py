"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#IssuerType``."""

from typing import Literal, TypeAlias, cast

IssuerType: TypeAlias = Literal[
    "ORIGINAL",
    "UPDATED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IssuerType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IssuerType:
    return cast(IssuerType, data)

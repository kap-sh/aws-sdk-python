"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#OAuthFlowType``."""

from typing import Literal, TypeAlias, cast

OAuthFlowType: TypeAlias = Literal[
    "code",
    "implicit",
    "client_credentials",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OAuthFlowType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OAuthFlowType:
    return cast(OAuthFlowType, data)

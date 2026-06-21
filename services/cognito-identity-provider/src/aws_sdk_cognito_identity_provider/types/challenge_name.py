"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ChallengeName``."""

from typing import Literal, TypeAlias, cast

ChallengeName: TypeAlias = Literal[
    "Password",
    "Mfa",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChallengeName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ChallengeName:
    return cast(ChallengeName, data)

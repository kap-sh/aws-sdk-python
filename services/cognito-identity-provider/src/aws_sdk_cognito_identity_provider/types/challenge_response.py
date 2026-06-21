"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ChallengeResponse``."""

from typing import Literal, TypeAlias, cast

ChallengeResponse: TypeAlias = Literal[
    "Success",
    "Failure",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChallengeResponse) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ChallengeResponse:
    return cast(ChallengeResponse, data)

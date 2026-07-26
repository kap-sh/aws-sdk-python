"""Generated from Smithy shape ``com.amazonaws.sagemaker#AuthMode``."""

from typing import Literal, TypeAlias, cast

AuthMode: TypeAlias = Literal[
    "SSO",
    "IAM",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AuthMode:
    return cast(AuthMode, data)

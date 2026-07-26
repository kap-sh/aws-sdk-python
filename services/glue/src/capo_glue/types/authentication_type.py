"""Generated from Smithy shape ``com.amazonaws.glue#AuthenticationType``."""

from typing import Literal, TypeAlias, cast

AuthenticationType: TypeAlias = Literal[
    "BASIC",
    "OAUTH2",
    "CUSTOM",
    "IAM",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthenticationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AuthenticationType:
    return cast(AuthenticationType, data)

"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#CompromisedCredentialsEventActionType``."""

from typing import Literal, TypeAlias, cast

CompromisedCredentialsEventActionType: TypeAlias = Literal[
    "BLOCK",
    "NO_ACTION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CompromisedCredentialsEventActionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CompromisedCredentialsEventActionType:
    return cast(CompromisedCredentialsEventActionType, data)

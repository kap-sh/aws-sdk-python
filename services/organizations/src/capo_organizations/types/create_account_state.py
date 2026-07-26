"""Generated from Smithy shape ``com.amazonaws.organizations#CreateAccountState``."""

from typing import Literal, TypeAlias, cast

CreateAccountState: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCEEDED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAccountState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CreateAccountState:
    return cast(CreateAccountState, data)

"""Generated from Smithy shape ``com.amazonaws.cloud9#ManagedCredentialsAction``."""

from typing import Literal, TypeAlias, cast

ManagedCredentialsAction: TypeAlias = Literal[
    "ENABLE",
    "DISABLE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedCredentialsAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ManagedCredentialsAction:
    return cast(ManagedCredentialsAction, data)

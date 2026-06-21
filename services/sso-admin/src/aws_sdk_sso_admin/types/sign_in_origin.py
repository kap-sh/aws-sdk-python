"""Generated from Smithy shape ``com.amazonaws.ssoadmin#SignInOrigin``."""

from typing import Literal, TypeAlias, cast

SignInOrigin: TypeAlias = Literal[
    "IDENTITY_CENTER",
    "APPLICATION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SignInOrigin) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SignInOrigin:
    return cast(SignInOrigin, data)

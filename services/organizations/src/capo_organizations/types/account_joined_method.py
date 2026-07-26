"""Generated from Smithy shape ``com.amazonaws.organizations#AccountJoinedMethod``."""

from typing import Literal, TypeAlias, cast

AccountJoinedMethod: TypeAlias = Literal[
    "INVITED",
    "CREATED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountJoinedMethod) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccountJoinedMethod:
    return cast(AccountJoinedMethod, data)

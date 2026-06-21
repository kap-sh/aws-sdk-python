"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#AuthTypeValue``."""

from typing import Literal, TypeAlias, cast

AuthTypeValue: TypeAlias = Literal[
    "no",
    "password",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthTypeValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AuthTypeValue:
    return cast(AuthTypeValue, data)

"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#MySQLAuthenticationMethod``."""

from typing import Literal, TypeAlias, cast

MySQLAuthenticationMethod: TypeAlias = Literal[
    "password",
    "iam",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MySQLAuthenticationMethod) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MySQLAuthenticationMethod:
    return cast(MySQLAuthenticationMethod, data)

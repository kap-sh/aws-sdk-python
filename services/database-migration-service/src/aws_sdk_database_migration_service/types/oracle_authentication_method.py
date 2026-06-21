"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#OracleAuthenticationMethod``."""

from typing import Literal, TypeAlias, cast

OracleAuthenticationMethod: TypeAlias = Literal[
    "password",
    "kerberos",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OracleAuthenticationMethod) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OracleAuthenticationMethod:
    return cast(OracleAuthenticationMethod, data)

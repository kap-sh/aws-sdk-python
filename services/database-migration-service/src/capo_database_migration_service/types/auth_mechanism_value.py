"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#AuthMechanismValue``."""

from typing import Literal, TypeAlias, cast

AuthMechanismValue: TypeAlias = Literal[
    "default",
    "mongodb_cr",
    "scram_sha_1",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthMechanismValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AuthMechanismValue:
    return cast(AuthMechanismValue, data)

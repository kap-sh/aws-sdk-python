"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#PreventUserExistenceErrorTypes``."""

from typing import Literal, TypeAlias, cast

PreventUserExistenceErrorTypes: TypeAlias = Literal[
    "LEGACY",
    "ENABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PreventUserExistenceErrorTypes) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PreventUserExistenceErrorTypes:
    return cast(PreventUserExistenceErrorTypes, data)

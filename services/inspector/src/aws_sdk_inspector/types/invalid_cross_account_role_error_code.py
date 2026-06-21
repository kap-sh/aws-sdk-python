"""Generated from Smithy shape ``com.amazonaws.inspector#InvalidCrossAccountRoleErrorCode``."""

from typing import Literal, TypeAlias, cast

InvalidCrossAccountRoleErrorCode: TypeAlias = Literal[
    "ROLE_DOES_NOT_EXIST_OR_INVALID_TRUST_RELATIONSHIP",
    "ROLE_DOES_NOT_HAVE_CORRECT_POLICY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidCrossAccountRoleErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InvalidCrossAccountRoleErrorCode:
    return cast(InvalidCrossAccountRoleErrorCode, data)

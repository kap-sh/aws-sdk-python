"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#RoleMappingType``."""

from typing import Literal, TypeAlias, cast

RoleMappingType: TypeAlias = Literal[
    "Token",
    "Rules",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RoleMappingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RoleMappingType:
    return cast(RoleMappingType, data)

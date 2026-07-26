"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#AmbiguousRoleResolutionType``."""

from typing import Literal, TypeAlias, cast

AmbiguousRoleResolutionType: TypeAlias = Literal[
    "AuthenticatedRole",
    "Deny",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AmbiguousRoleResolutionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AmbiguousRoleResolutionType:
    return cast(AmbiguousRoleResolutionType, data)

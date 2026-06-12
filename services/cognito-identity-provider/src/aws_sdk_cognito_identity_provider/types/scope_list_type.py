"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ScopeListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.scope_type

ScopeListType: TypeAlias = list[
    "aws_sdk_cognito_identity_provider.types.scope_type.ScopeType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScopeListType) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ScopeListType:
    return list(data)

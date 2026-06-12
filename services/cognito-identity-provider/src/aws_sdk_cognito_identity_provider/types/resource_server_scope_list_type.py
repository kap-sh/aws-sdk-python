"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ResourceServerScopeListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.resource_server_scope_type

ResourceServerScopeListType: TypeAlias = list[
    "aws_sdk_cognito_identity_provider.types.resource_server_scope_type.ResourceServerScopeType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceServerScopeListType) -> list:
    import aws_sdk_cognito_identity_provider.types.resource_server_scope_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cognito_identity_provider.types.resource_server_scope_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceServerScopeListType:
    import aws_sdk_cognito_identity_provider.types.resource_server_scope_type

    out: ResourceServerScopeListType = []
    for item in data:
        out.append(
            aws_sdk_cognito_identity_provider.types.resource_server_scope_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out

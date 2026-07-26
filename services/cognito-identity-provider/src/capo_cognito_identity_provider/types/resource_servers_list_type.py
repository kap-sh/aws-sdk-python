"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ResourceServersListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.resource_server_type

ResourceServersListType: TypeAlias = list[
    "capo_cognito_identity_provider.types.resource_server_type.ResourceServerType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceServersListType) -> list:
    import capo_cognito_identity_provider.types.resource_server_type

    out: list = []
    for item in value:
        out.append(
            capo_cognito_identity_provider.types.resource_server_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceServersListType:
    import capo_cognito_identity_provider.types.resource_server_type

    out: ResourceServersListType = []
    for item in data:
        out.append(
            capo_cognito_identity_provider.types.resource_server_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out

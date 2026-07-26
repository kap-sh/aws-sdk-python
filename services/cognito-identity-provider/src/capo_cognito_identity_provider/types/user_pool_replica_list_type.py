"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UserPoolReplicaListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.user_pool_replica_type

UserPoolReplicaListType: TypeAlias = list[
    "capo_cognito_identity_provider.types.user_pool_replica_type.UserPoolReplicaType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserPoolReplicaListType) -> list:
    import capo_cognito_identity_provider.types.user_pool_replica_type

    out: list = []
    for item in value:
        out.append(
            capo_cognito_identity_provider.types.user_pool_replica_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UserPoolReplicaListType:
    import capo_cognito_identity_provider.types.user_pool_replica_type

    out: UserPoolReplicaListType = []
    for item in data:
        out.append(
            capo_cognito_identity_provider.types.user_pool_replica_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#CreateUserPoolReplicaResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.user_pool_replica_type


class CreateUserPoolReplicaResponse(TypedDict, closed=True):
    user_pool_replica: NotRequired[
        "capo_cognito_identity_provider.types.user_pool_replica_type.UserPoolReplicaType"
    ]
    """<p>Information about the created user pool replica, including its status and role.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateUserPoolReplicaResponse) -> dict:
    out: dict = {}
    if "user_pool_replica" in value:
        import capo_cognito_identity_provider.types.user_pool_replica_type

        out["UserPoolReplica"] = (
            capo_cognito_identity_provider.types.user_pool_replica_type.serialize_aws_json_1_1(
                value["user_pool_replica"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateUserPoolReplicaResponse:
    out: CreateUserPoolReplicaResponse = {}  # type: ignore[typeddict-item]
    if "UserPoolReplica" in data:
        import capo_cognito_identity_provider.types.user_pool_replica_type

        out["user_pool_replica"] = (
            capo_cognito_identity_provider.types.user_pool_replica_type.deserialize_aws_json_1_1(
                data["UserPoolReplica"]
            )
        )
    return out

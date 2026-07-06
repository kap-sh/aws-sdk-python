"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UpdateUserPoolReplicaResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.user_pool_replica_type


class UpdateUserPoolReplicaResponse(TypedDict, closed=True):
    user_pool_replica: NotRequired[
        "aws_sdk_cognito_identity_provider.types.user_pool_replica_type.UserPoolReplicaType"
    ]
    """<p>Information about the updated user pool replica.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateUserPoolReplicaResponse) -> dict:
    out: dict = {}
    if "user_pool_replica" in value:
        import aws_sdk_cognito_identity_provider.types.user_pool_replica_type

        out["UserPoolReplica"] = (
            aws_sdk_cognito_identity_provider.types.user_pool_replica_type.serialize_aws_json_1_1(
                value["user_pool_replica"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateUserPoolReplicaResponse:
    out: UpdateUserPoolReplicaResponse = {}  # type: ignore[typeddict-item]
    if "UserPoolReplica" in data:
        import aws_sdk_cognito_identity_provider.types.user_pool_replica_type

        out["user_pool_replica"] = (
            aws_sdk_cognito_identity_provider.types.user_pool_replica_type.deserialize_aws_json_1_1(
                data["UserPoolReplica"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ListUserPoolReplicasResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.pagination_key_type
    import capo_cognito_identity_provider.types.user_pool_replica_list_type


class ListUserPoolReplicasResponse(TypedDict, closed=True):
    user_pool_replicas: NotRequired[
        "capo_cognito_identity_provider.types.user_pool_replica_list_type.UserPoolReplicaListType"
    ]
    """<p>A list of user pool replicas, including information about their status, role, and Region.</p>"""
    next_token: NotRequired[
        "capo_cognito_identity_provider.types.pagination_key_type.PaginationKeyType"
    ]
    """<p>A pagination token for retrieving the next page of results. If this value is null, there are no more results to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListUserPoolReplicasResponse) -> dict:
    out: dict = {}
    if "user_pool_replicas" in value:
        import capo_cognito_identity_provider.types.user_pool_replica_list_type

        out["UserPoolReplicas"] = (
            capo_cognito_identity_provider.types.user_pool_replica_list_type.serialize_aws_json_1_1(
                value["user_pool_replicas"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListUserPoolReplicasResponse:
    out: ListUserPoolReplicasResponse = {}  # type: ignore[typeddict-item]
    if "UserPoolReplicas" in data:
        import capo_cognito_identity_provider.types.user_pool_replica_list_type

        out["user_pool_replicas"] = (
            capo_cognito_identity_provider.types.user_pool_replica_list_type.deserialize_aws_json_1_1(
                data["UserPoolReplicas"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

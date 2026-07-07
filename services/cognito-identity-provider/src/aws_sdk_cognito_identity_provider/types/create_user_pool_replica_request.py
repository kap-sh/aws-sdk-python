"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#CreateUserPoolReplicaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.region_name_type
    import aws_sdk_cognito_identity_provider.types.user_pool_id_type
    import aws_sdk_cognito_identity_provider.types.user_pool_tags_type


class CreateUserPoolReplicaRequest(TypedDict, closed=True):
    user_pool_id: (
        "aws_sdk_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool to replicate.</p>"""
    region_name: (
        "aws_sdk_cognito_identity_provider.types.region_name_type.RegionNameType"
    )
    """<p>The Amazon Web Services Region where you want to create the replica user pool.</p>"""
    user_pool_tags: NotRequired[
        "aws_sdk_cognito_identity_provider.types.user_pool_tags_type.UserPoolTagsType"
    ]
    """<p>A map of tags to assign to the replica user pool. Each tag consists of a key and an optional value, both of which you define. You can maintain tags independently on replica user pools.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateUserPoolReplicaRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["RegionName"] = value["region_name"]
    if "user_pool_tags" in value:
        import aws_sdk_cognito_identity_provider.types.user_pool_tags_type

        out["UserPoolTags"] = (
            aws_sdk_cognito_identity_provider.types.user_pool_tags_type.serialize_aws_json_1_1(
                value["user_pool_tags"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateUserPoolReplicaRequest:
    out: CreateUserPoolReplicaRequest = {}  # type: ignore[typeddict-item]
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError("CreateUserPoolReplicaRequest.user_pool_id required")
    if "RegionName" in data:
        out["region_name"] = data["RegionName"]
    else:
        raise DeserializationError("CreateUserPoolReplicaRequest.region_name required")
    if "UserPoolTags" in data:
        import aws_sdk_cognito_identity_provider.types.user_pool_tags_type

        out["user_pool_tags"] = (
            aws_sdk_cognito_identity_provider.types.user_pool_tags_type.deserialize_aws_json_1_1(
                data["UserPoolTags"]
            )
        )
    return out

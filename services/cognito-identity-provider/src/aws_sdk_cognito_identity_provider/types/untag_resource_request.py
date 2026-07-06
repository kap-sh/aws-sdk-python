"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.arn_type
    import aws_sdk_cognito_identity_provider.types.user_pool_tags_list_type


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_cognito_identity_provider.types.arn_type.ArnType"
    """<p>The Amazon Resource Name (ARN) of the user pool that the tags are assigned to.</p>"""
    tag_keys: "aws_sdk_cognito_identity_provider.types.user_pool_tags_list_type.UserPoolTagsListType"
    """<p>An array of tag keys that you want to remove from the user pool.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import aws_sdk_cognito_identity_provider.types.user_pool_tags_list_type

    out["TagKeys"] = (
        aws_sdk_cognito_identity_provider.types.user_pool_tags_list_type.serialize_aws_json_1_1(
            value["tag_keys"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if "TagKeys" in data:
        import aws_sdk_cognito_identity_provider.types.user_pool_tags_list_type

        out["tag_keys"] = (
            aws_sdk_cognito_identity_provider.types.user_pool_tags_list_type.deserialize_aws_json_1_1(
                data["TagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out

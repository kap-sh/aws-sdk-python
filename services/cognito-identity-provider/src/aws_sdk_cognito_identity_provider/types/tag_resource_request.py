"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.arn_type
    import aws_sdk_cognito_identity_provider.types.user_pool_tags_type


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_cognito_identity_provider.types.arn_type.ArnType"
    """<p>The Amazon Resource Name (ARN) of the user pool to assign the tags to.</p>"""
    tags: "aws_sdk_cognito_identity_provider.types.user_pool_tags_type.UserPoolTagsType"
    """<p>An array of tag keys and values that you want to assign to the user pool.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import aws_sdk_cognito_identity_provider.types.user_pool_tags_type

    out["Tags"] = (
        aws_sdk_cognito_identity_provider.types.user_pool_tags_type.serialize_aws_json_1_1(
            value["tags"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "Tags" in data:
        import aws_sdk_cognito_identity_provider.types.user_pool_tags_type

        out["tags"] = (
            aws_sdk_cognito_identity_provider.types.user_pool_tags_type.deserialize_aws_json_1_1(
                data["Tags"]
            )
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#UntagResourceInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cognito_identity.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity.types.arn_string
    import aws_sdk_cognito_identity.types.identity_pool_tags_list_type


class UntagResourceInput(TypedDict):
    resource_arn: "aws_sdk_cognito_identity.types.arn_string.ARNString"
    """<p>The Amazon Resource Name (ARN) of the identity pool.</p>"""
    tag_keys: "aws_sdk_cognito_identity.types.identity_pool_tags_list_type.IdentityPoolTagsListType"
    """<p>The keys of the tags to remove from the user pool.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceInput) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import aws_sdk_cognito_identity.types.identity_pool_tags_list_type

    out["TagKeys"] = (
        aws_sdk_cognito_identity.types.identity_pool_tags_list_type.serialize_aws_json_1_1(
            value["tag_keys"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("UntagResourceInput.resource_arn required")
    if "TagKeys" in data:
        import aws_sdk_cognito_identity.types.identity_pool_tags_list_type

        out["tag_keys"] = (
            aws_sdk_cognito_identity.types.identity_pool_tags_list_type.deserialize_aws_json_1_1(
                data["TagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceInput.tag_keys required")
    return out

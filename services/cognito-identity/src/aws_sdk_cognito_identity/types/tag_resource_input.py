"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cognito_identity.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity.types.arn_string
    import aws_sdk_cognito_identity.types.identity_pool_tags_type


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "aws_sdk_cognito_identity.types.arn_string.ARNString"
    """<p>The Amazon Resource Name (ARN) of the identity pool.</p>"""
    tags: "aws_sdk_cognito_identity.types.identity_pool_tags_type.IdentityPoolTagsType"
    """<p>The tags to assign to the identity pool.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceInput) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import aws_sdk_cognito_identity.types.identity_pool_tags_type

    out["Tags"] = (
        aws_sdk_cognito_identity.types.identity_pool_tags_type.serialize_aws_json_1_1(
            value["tags"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("TagResourceInput.resource_arn required")
    if "Tags" in data:
        import aws_sdk_cognito_identity.types.identity_pool_tags_type

        out["tags"] = (
            aws_sdk_cognito_identity.types.identity_pool_tags_type.deserialize_aws_json_1_1(
                data["Tags"]
            )
        )
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out

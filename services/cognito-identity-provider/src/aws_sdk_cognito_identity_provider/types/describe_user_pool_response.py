"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DescribeUserPoolResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.user_pool_type


class DescribeUserPoolResponse(TypedDict, closed=True):
    user_pool: NotRequired[
        "aws_sdk_cognito_identity_provider.types.user_pool_type.UserPoolType"
    ]
    """<p>The details of the requested user pool.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeUserPoolResponse) -> dict:
    out: dict = {}
    if "user_pool" in value:
        import aws_sdk_cognito_identity_provider.types.user_pool_type

        out["UserPool"] = (
            aws_sdk_cognito_identity_provider.types.user_pool_type.serialize_aws_json_1_1(
                value["user_pool"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeUserPoolResponse:
    out: DescribeUserPoolResponse = {}  # type: ignore[typeddict-item]
    if "UserPool" in data:
        import aws_sdk_cognito_identity_provider.types.user_pool_type

        out["user_pool"] = (
            aws_sdk_cognito_identity_provider.types.user_pool_type.deserialize_aws_json_1_1(
                data["UserPool"]
            )
        )
    return out

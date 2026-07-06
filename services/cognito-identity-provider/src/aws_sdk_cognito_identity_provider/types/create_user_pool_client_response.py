"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#CreateUserPoolClientResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.user_pool_client_type


class CreateUserPoolClientResponse(TypedDict, closed=True):
    user_pool_client: NotRequired[
        "aws_sdk_cognito_identity_provider.types.user_pool_client_type.UserPoolClientType"
    ]
    """<p>The details of the new app client.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateUserPoolClientResponse) -> dict:
    out: dict = {}
    if "user_pool_client" in value:
        import aws_sdk_cognito_identity_provider.types.user_pool_client_type

        out["UserPoolClient"] = (
            aws_sdk_cognito_identity_provider.types.user_pool_client_type.serialize_aws_json_1_1(
                value["user_pool_client"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateUserPoolClientResponse:
    out: CreateUserPoolClientResponse = {}  # type: ignore[typeddict-item]
    if "UserPoolClient" in data:
        import aws_sdk_cognito_identity_provider.types.user_pool_client_type

        out["user_pool_client"] = (
            aws_sdk_cognito_identity_provider.types.user_pool_client_type.deserialize_aws_json_1_1(
                data["UserPoolClient"]
            )
        )
    return out

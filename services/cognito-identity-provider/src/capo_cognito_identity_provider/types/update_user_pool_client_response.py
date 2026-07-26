"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UpdateUserPoolClientResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.user_pool_client_type


class UpdateUserPoolClientResponse(TypedDict, closed=True):
    user_pool_client: NotRequired[
        "capo_cognito_identity_provider.types.user_pool_client_type.UserPoolClientType"
    ]
    """<p>The updated details of your app client.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateUserPoolClientResponse) -> dict:
    out: dict = {}
    if "user_pool_client" in value:
        import capo_cognito_identity_provider.types.user_pool_client_type

        out["UserPoolClient"] = (
            capo_cognito_identity_provider.types.user_pool_client_type.serialize_aws_json_1_1(
                value["user_pool_client"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateUserPoolClientResponse:
    out: UpdateUserPoolClientResponse = {}  # type: ignore[typeddict-item]
    if "UserPoolClient" in data:
        import capo_cognito_identity_provider.types.user_pool_client_type

        out["user_pool_client"] = (
            capo_cognito_identity_provider.types.user_pool_client_type.deserialize_aws_json_1_1(
                data["UserPoolClient"]
            )
        )
    return out

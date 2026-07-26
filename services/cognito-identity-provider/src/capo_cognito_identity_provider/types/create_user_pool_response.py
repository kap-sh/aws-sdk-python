"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#CreateUserPoolResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.user_pool_type


class CreateUserPoolResponse(TypedDict, closed=True):
    user_pool: NotRequired[
        "capo_cognito_identity_provider.types.user_pool_type.UserPoolType"
    ]
    """<p>The details of the created user pool.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateUserPoolResponse) -> dict:
    out: dict = {}
    if "user_pool" in value:
        import capo_cognito_identity_provider.types.user_pool_type

        out["UserPool"] = (
            capo_cognito_identity_provider.types.user_pool_type.serialize_aws_json_1_1(
                value["user_pool"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateUserPoolResponse:
    out: CreateUserPoolResponse = {}  # type: ignore[typeddict-item]
    if "UserPool" in data:
        import capo_cognito_identity_provider.types.user_pool_type

        out["user_pool"] = (
            capo_cognito_identity_provider.types.user_pool_type.deserialize_aws_json_1_1(
                data["UserPool"]
            )
        )
    return out

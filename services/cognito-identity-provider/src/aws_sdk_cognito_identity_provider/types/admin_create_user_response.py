"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AdminCreateUserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.user_type


class AdminCreateUserResponse(TypedDict, closed=True):
    user: NotRequired["aws_sdk_cognito_identity_provider.types.user_type.UserType"]
    """<p>The new user's profile details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdminCreateUserResponse) -> dict:
    out: dict = {}
    if "user" in value:
        import aws_sdk_cognito_identity_provider.types.user_type

        out["User"] = (
            aws_sdk_cognito_identity_provider.types.user_type.serialize_aws_json_1_1(
                value["user"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AdminCreateUserResponse:
    out: AdminCreateUserResponse = {}  # type: ignore[typeddict-item]
    if "User" in data:
        import aws_sdk_cognito_identity_provider.types.user_type

        out["user"] = (
            aws_sdk_cognito_identity_provider.types.user_type.deserialize_aws_json_1_1(
                data["User"]
            )
        )
    return out

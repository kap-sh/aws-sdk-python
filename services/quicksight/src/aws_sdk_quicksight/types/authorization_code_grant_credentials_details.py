"""Generated from Smithy shape ``com.amazonaws.quicksight#AuthorizationCodeGrantCredentialsDetails``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_quicksight.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.authorization_code_grant_details


class _AuthorizationCodeGrantCredentialsDetails_AuthorizationCodeGrantDetails(
    TypedDict
):
    AuthorizationCodeGrantDetails: "aws_sdk_quicksight.types.authorization_code_grant_details.AuthorizationCodeGrantDetails"


AuthorizationCodeGrantCredentialsDetails: TypeAlias = (
    _AuthorizationCodeGrantCredentialsDetails_AuthorizationCodeGrantDetails
)


# --- restJson1 ser/de ---
def serialize_json(value: AuthorizationCodeGrantCredentialsDetails) -> dict:
    if "AuthorizationCodeGrantDetails" in value:
        import aws_sdk_quicksight.types.authorization_code_grant_details

        return {
            "AuthorizationCodeGrantDetails": aws_sdk_quicksight.types.authorization_code_grant_details.serialize_json(
                value["AuthorizationCodeGrantDetails"]
            )
        }
    else:
        raise SerializationError(
            "AuthorizationCodeGrantCredentialsDetails: no variant present"
        )


def deserialize_json(data: dict) -> AuthorizationCodeGrantCredentialsDetails:
    if "AuthorizationCodeGrantDetails" in data:
        import aws_sdk_quicksight.types.authorization_code_grant_details

        return {
            "AuthorizationCodeGrantDetails": aws_sdk_quicksight.types.authorization_code_grant_details.deserialize_json(
                data["AuthorizationCodeGrantDetails"]
            )
        }
    else:
        raise DeserializationError(
            "AuthorizationCodeGrantCredentialsDetails: no recognized variant key"
        )

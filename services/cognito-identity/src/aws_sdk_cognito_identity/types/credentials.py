"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#Credentials``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_identity.types.access_key_string
    import aws_sdk_cognito_identity.types.date_type
    import aws_sdk_cognito_identity.types.secret_key_string
    import aws_sdk_cognito_identity.types.session_token_string


class Credentials(TypedDict, closed=True):
    access_key_id: NotRequired[
        "aws_sdk_cognito_identity.types.access_key_string.AccessKeyString"
    ]
    """<p>The Access Key portion of the credentials.</p>"""
    secret_key: NotRequired[
        "aws_sdk_cognito_identity.types.secret_key_string.SecretKeyString"
    ]
    """<p>The Secret Access Key portion of the credentials</p>"""
    session_token: NotRequired[
        "aws_sdk_cognito_identity.types.session_token_string.SessionTokenString"
    ]
    """<p>The Session Token portion of the credentials</p>"""
    expiration: NotRequired["aws_sdk_cognito_identity.types.date_type.DateType"]
    """<p>The date at which these credentials will expire.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Credentials) -> dict:
    out: dict = {}
    if "access_key_id" in value:
        out["AccessKeyId"] = value["access_key_id"]
    if "secret_key" in value:
        out["SecretKey"] = value["secret_key"]
    if "session_token" in value:
        out["SessionToken"] = value["session_token"]
    if "expiration" in value:
        import aws_sdk_cognito_identity.types.date_type

        out["Expiration"] = (
            aws_sdk_cognito_identity.types.date_type.serialize_aws_json_1_1(
                value["expiration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Credentials:
    out: Credentials = {}  # type: ignore[typeddict-item]
    if "AccessKeyId" in data:
        out["access_key_id"] = data["AccessKeyId"]
    if "SecretKey" in data:
        out["secret_key"] = data["SecretKey"]
    if "SessionToken" in data:
        out["session_token"] = data["SessionToken"]
    if "Expiration" in data:
        import aws_sdk_cognito_identity.types.date_type

        out["expiration"] = (
            aws_sdk_cognito_identity.types.date_type.deserialize_aws_json_1_1(
                data["Expiration"]
            )
        )
    return out

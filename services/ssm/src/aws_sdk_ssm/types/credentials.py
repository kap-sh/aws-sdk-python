"""Generated from Smithy shape ``com.amazonaws.ssm#Credentials``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.access_key_id_type
    import aws_sdk_ssm.types.access_key_secret_type
    import aws_sdk_ssm.types.date_time
    import aws_sdk_ssm.types.session_token_type


class Credentials(TypedDict, closed=True):
    access_key_id: "aws_sdk_ssm.types.access_key_id_type.AccessKeyIdType"
    """<p>The access key ID that identifies the temporary security credentials.</p>"""
    secret_access_key: "aws_sdk_ssm.types.access_key_secret_type.AccessKeySecretType"
    """<p>The secret access key that can be used to sign requests.</p>"""
    session_token: "aws_sdk_ssm.types.session_token_type.SessionTokenType"
    """<p>The token that users must pass to the service API to use the temporary credentials.</p>"""
    expiration_time: "aws_sdk_ssm.types.date_time.DateTime"
    """<p>The datetime on which the current credentials expire.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Credentials) -> dict:
    out: dict = {}
    out["AccessKeyId"] = value["access_key_id"]
    out["SecretAccessKey"] = value["secret_access_key"]
    out["SessionToken"] = value["session_token"]
    import aws_sdk_ssm.types.date_time

    out["ExpirationTime"] = aws_sdk_ssm.types.date_time.serialize_aws_json_1_1(
        value["expiration_time"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Credentials:
    out: Credentials = {}  # type: ignore[typeddict-item]
    if "AccessKeyId" in data:
        out["access_key_id"] = data["AccessKeyId"]
    else:
        raise DeserializationError("Credentials.access_key_id required")
    if "SecretAccessKey" in data:
        out["secret_access_key"] = data["SecretAccessKey"]
    else:
        raise DeserializationError("Credentials.secret_access_key required")
    if "SessionToken" in data:
        out["session_token"] = data["SessionToken"]
    else:
        raise DeserializationError("Credentials.session_token required")
    if "ExpirationTime" in data:
        import aws_sdk_ssm.types.date_time

        out["expiration_time"] = aws_sdk_ssm.types.date_time.deserialize_aws_json_1_1(
            data["ExpirationTime"]
        )
    else:
        raise DeserializationError("Credentials.expiration_time required")
    return out

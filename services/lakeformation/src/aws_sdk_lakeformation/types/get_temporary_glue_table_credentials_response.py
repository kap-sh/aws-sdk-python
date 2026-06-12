"""Generated from Smithy shape ``com.amazonaws.lakeformation#GetTemporaryGlueTableCredentialsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.access_key_id_string
    import aws_sdk_lakeformation.types.expiration_timestamp
    import aws_sdk_lakeformation.types.path_string_list
    import aws_sdk_lakeformation.types.secret_access_key_string
    import aws_sdk_lakeformation.types.session_token_string


class GetTemporaryGlueTableCredentialsResponse(TypedDict):
    access_key_id: NotRequired[
        "aws_sdk_lakeformation.types.access_key_id_string.AccessKeyIdString"
    ]
    """<p>The access key ID for the temporary credentials.</p>"""
    secret_access_key: NotRequired[
        "aws_sdk_lakeformation.types.secret_access_key_string.SecretAccessKeyString"
    ]
    """<p>The secret key for the temporary credentials.</p>"""
    session_token: NotRequired[
        "aws_sdk_lakeformation.types.session_token_string.SessionTokenString"
    ]
    """<p>The session token for the temporary credentials.</p>"""
    expiration: NotRequired[
        "aws_sdk_lakeformation.types.expiration_timestamp.ExpirationTimestamp"
    ]
    """<p>The date and time when the temporary credentials expire.</p>"""
    vended_s3_path: NotRequired[
        "aws_sdk_lakeformation.types.path_string_list.PathStringList"
    ]
    """<p>The Amazon S3 path for the temporary credentials.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTemporaryGlueTableCredentialsResponse) -> dict:
    out: dict = {}
    if "access_key_id" in value:
        out["AccessKeyId"] = value["access_key_id"]
    if "secret_access_key" in value:
        out["SecretAccessKey"] = value["secret_access_key"]
    if "session_token" in value:
        out["SessionToken"] = value["session_token"]
    if "expiration" in value:
        import aws_sdk_lakeformation.types.expiration_timestamp

        out["Expiration"] = (
            aws_sdk_lakeformation.types.expiration_timestamp.serialize_json(
                value["expiration"]
            )
        )
    if "vended_s3_path" in value:
        import aws_sdk_lakeformation.types.path_string_list

        out["VendedS3Path"] = (
            aws_sdk_lakeformation.types.path_string_list.serialize_json(
                value["vended_s3_path"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetTemporaryGlueTableCredentialsResponse:
    out: GetTemporaryGlueTableCredentialsResponse = {}  # type: ignore[typeddict-item]
    if "AccessKeyId" in data:
        out["access_key_id"] = data["AccessKeyId"]
    if "SecretAccessKey" in data:
        out["secret_access_key"] = data["SecretAccessKey"]
    if "SessionToken" in data:
        out["session_token"] = data["SessionToken"]
    if "Expiration" in data:
        import aws_sdk_lakeformation.types.expiration_timestamp

        out["expiration"] = (
            aws_sdk_lakeformation.types.expiration_timestamp.deserialize_json(
                data["Expiration"]
            )
        )
    if "VendedS3Path" in data:
        import aws_sdk_lakeformation.types.path_string_list

        out["vended_s3_path"] = (
            aws_sdk_lakeformation.types.path_string_list.deserialize_json(
                data["VendedS3Path"]
            )
        )
    return out

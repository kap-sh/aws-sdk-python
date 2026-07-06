"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#GetCredentialsForIdentityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_identity.types.credentials
    import aws_sdk_cognito_identity.types.identity_id


class GetCredentialsForIdentityResponse(TypedDict, closed=True):
    identity_id: NotRequired["aws_sdk_cognito_identity.types.identity_id.IdentityId"]
    """<p>A unique identifier in the format REGION:GUID.</p>"""
    credentials: NotRequired["aws_sdk_cognito_identity.types.credentials.Credentials"]
    """<p>Credentials for the provided identity ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCredentialsForIdentityResponse) -> dict:
    out: dict = {}
    if "identity_id" in value:
        out["IdentityId"] = value["identity_id"]
    if "credentials" in value:
        import aws_sdk_cognito_identity.types.credentials

        out["Credentials"] = (
            aws_sdk_cognito_identity.types.credentials.serialize_aws_json_1_1(
                value["credentials"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCredentialsForIdentityResponse:
    out: GetCredentialsForIdentityResponse = {}  # type: ignore[typeddict-item]
    if "IdentityId" in data:
        out["identity_id"] = data["IdentityId"]
    if "Credentials" in data:
        import aws_sdk_cognito_identity.types.credentials

        out["credentials"] = (
            aws_sdk_cognito_identity.types.credentials.deserialize_aws_json_1_1(
                data["Credentials"]
            )
        )
    return out

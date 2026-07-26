"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#GetSigningCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.user_pool_id_type


class GetSigningCertificateRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool where you want to view the signing certificate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSigningCertificateRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSigningCertificateRequest:
    out: GetSigningCertificateRequest = {}  # type: ignore[typeddict-item]
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError("GetSigningCertificateRequest.user_pool_id required")
    return out

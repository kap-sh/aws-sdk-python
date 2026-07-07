"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#GetSigningCertificateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.string_type


class GetSigningCertificateResponse(TypedDict, closed=True):
    certificate: NotRequired[
        "aws_sdk_cognito_identity_provider.types.string_type.StringType"
    ]
    """<p>The x.509 certificate that signs SAML 2.0 authentication requests for your user pool.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSigningCertificateResponse) -> dict:
    out: dict = {}
    if "certificate" in value:
        out["Certificate"] = value["certificate"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSigningCertificateResponse:
    out: GetSigningCertificateResponse = {}  # type: ignore[typeddict-item]
    if "Certificate" in data:
        out["certificate"] = data["Certificate"]
    return out

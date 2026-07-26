"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#CustomDomainConfigType``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.arn_type


class CustomDomainConfigType(TypedDict, closed=True):
    certificate_arn: "capo_cognito_identity_provider.types.arn_type.ArnType"
    """<p>The Amazon Resource Name (ARN) of an Certificate Manager SSL certificate. You use this certificate for the subdomain of your custom domain.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomDomainConfigType) -> dict:
    out: dict = {}
    out["CertificateArn"] = value["certificate_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomDomainConfigType:
    out: CustomDomainConfigType = {}  # type: ignore[typeddict-item]
    if "CertificateArn" in data:
        out["certificate_arn"] = data["CertificateArn"]
    else:
        raise DeserializationError("CustomDomainConfigType.certificate_arn required")
    return out

"""Generated from Smithy shape ``com.amazonaws.acm#RequestCertificateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_acm.types.arn


class RequestCertificateResponse(TypedDict):
    certificate_arn: NotRequired["aws_sdk_acm.types.arn.Arn"]
    """<p>String that contains the ARN of the issued certificate. This must be of the form:</p> <p> <code>arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RequestCertificateResponse) -> dict:
    out: dict = {}
    if "certificate_arn" in value:
        out["CertificateArn"] = value["certificate_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RequestCertificateResponse:
    out: RequestCertificateResponse = {}  # type: ignore[typeddict-item]
    if "CertificateArn" in data:
        out["certificate_arn"] = data["CertificateArn"]
    return out

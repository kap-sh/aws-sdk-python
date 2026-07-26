"""Generated from Smithy shape ``com.amazonaws.acm#RevokeCertificateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.arn


class RevokeCertificateResponse(TypedDict, closed=True):
    certificate_arn: NotRequired["capo_acm.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the public or private certificate that was revoked.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RevokeCertificateResponse) -> dict:
    out: dict = {}
    if "certificate_arn" in value:
        out["CertificateArn"] = value["certificate_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RevokeCertificateResponse:
    out: RevokeCertificateResponse = {}  # type: ignore[typeddict-item]
    if "CertificateArn" in data:
        out["certificate_arn"] = data["CertificateArn"]
    return out

"""Generated from Smithy shape ``com.amazonaws.acm#ImportCertificateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_acm.types.arn


class ImportCertificateResponse(TypedDict):
    certificate_arn: NotRequired["aws_sdk_acm.types.arn.Arn"]
    r"""<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Name (ARN)</a> of the imported certificate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportCertificateResponse) -> dict:
    out: dict = {}
    if "certificate_arn" in value:
        out["CertificateArn"] = value["certificate_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportCertificateResponse:
    out: ImportCertificateResponse = {}  # type: ignore[typeddict-item]
    if "CertificateArn" in data:
        out["certificate_arn"] = data["CertificateArn"]
    return out

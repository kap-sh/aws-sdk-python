"""Generated from Smithy shape ``com.amazonaws.acmpca#DeleteCertificateAuthorityRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_acm_pca.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_acm_pca.types.arn
    import aws_sdk_acm_pca.types.permanent_deletion_time_in_days


class DeleteCertificateAuthorityRequest(TypedDict):
    certificate_authority_arn: "aws_sdk_acm_pca.types.arn.Arn"
    r"""<p>The Amazon Resource Name (ARN) that was returned when you called <a href=\"https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html\">CreateCertificateAuthority</a>. This must have the following form: </p> <p> <code>arn:aws:acm-pca:<i>region</i>:<i>account</i>:certificate-authority/<i>12345678-1234-1234-1234-123456789012</i> </code>. </p>"""
    permanent_deletion_time_in_days: NotRequired[
        "aws_sdk_acm_pca.types.permanent_deletion_time_in_days.PermanentDeletionTimeInDays"
    ]
    """<p>The number of days to make a CA restorable after it has been deleted. This can be anywhere from 7 to 30 days, with 30 being the default.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteCertificateAuthorityRequest) -> dict:
    out: dict = {}
    out["CertificateAuthorityArn"] = value["certificate_authority_arn"]
    if "permanent_deletion_time_in_days" in value:
        out["PermanentDeletionTimeInDays"] = value["permanent_deletion_time_in_days"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteCertificateAuthorityRequest:
    out: DeleteCertificateAuthorityRequest = {}  # type: ignore[typeddict-item]
    if "CertificateAuthorityArn" in data:
        out["certificate_authority_arn"] = data["CertificateAuthorityArn"]
    else:
        raise DeserializationError(
            "DeleteCertificateAuthorityRequest.certificate_authority_arn required"
        )
    if "PermanentDeletionTimeInDays" in data:
        out["permanent_deletion_time_in_days"] = data["PermanentDeletionTimeInDays"]
    return out

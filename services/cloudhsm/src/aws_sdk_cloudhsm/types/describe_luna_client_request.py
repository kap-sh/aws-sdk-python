"""Generated from Smithy shape ``com.amazonaws.cloudhsm#DescribeLunaClientRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudhsm.types.certificate_fingerprint
    import aws_sdk_cloudhsm.types.client_arn


class DescribeLunaClientRequest(TypedDict, closed=True):
    client_arn: NotRequired["aws_sdk_cloudhsm.types.client_arn.ClientArn"]
    """<p>The ARN of the client.</p>"""
    certificate_fingerprint: NotRequired[
        "aws_sdk_cloudhsm.types.certificate_fingerprint.CertificateFingerprint"
    ]
    """<p>The certificate fingerprint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLunaClientRequest) -> dict:
    out: dict = {}
    if "client_arn" in value:
        out["ClientArn"] = value["client_arn"]
    if "certificate_fingerprint" in value:
        out["CertificateFingerprint"] = value["certificate_fingerprint"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLunaClientRequest:
    out: DescribeLunaClientRequest = {}  # type: ignore[typeddict-item]
    if "ClientArn" in data:
        out["client_arn"] = data["ClientArn"]
    if "CertificateFingerprint" in data:
        out["certificate_fingerprint"] = data["CertificateFingerprint"]
    return out

"""Generated from Smithy shape ``com.amazonaws.cloudhsm#DescribeLunaClientResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudhsm.types.certificate
    import aws_sdk_cloudhsm.types.certificate_fingerprint
    import aws_sdk_cloudhsm.types.client_arn
    import aws_sdk_cloudhsm.types.label
    import aws_sdk_cloudhsm.types.timestamp


class DescribeLunaClientResponse(TypedDict, closed=True):
    client_arn: NotRequired["aws_sdk_cloudhsm.types.client_arn.ClientArn"]
    """<p>The ARN of the client.</p>"""
    certificate: NotRequired["aws_sdk_cloudhsm.types.certificate.Certificate"]
    """<p>The certificate installed on the HSMs used by this client.</p>"""
    certificate_fingerprint: NotRequired[
        "aws_sdk_cloudhsm.types.certificate_fingerprint.CertificateFingerprint"
    ]
    """<p>The certificate fingerprint.</p>"""
    last_modified_timestamp: NotRequired["aws_sdk_cloudhsm.types.timestamp.Timestamp"]
    """<p>The date and time the client was last modified.</p>"""
    label: NotRequired["aws_sdk_cloudhsm.types.label.Label"]
    """<p>The label of the client.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLunaClientResponse) -> dict:
    out: dict = {}
    if "client_arn" in value:
        out["ClientArn"] = value["client_arn"]
    if "certificate" in value:
        out["Certificate"] = value["certificate"]
    if "certificate_fingerprint" in value:
        out["CertificateFingerprint"] = value["certificate_fingerprint"]
    if "last_modified_timestamp" in value:
        out["LastModifiedTimestamp"] = value["last_modified_timestamp"]
    if "label" in value:
        out["Label"] = value["label"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLunaClientResponse:
    out: DescribeLunaClientResponse = {}  # type: ignore[typeddict-item]
    if "ClientArn" in data:
        out["client_arn"] = data["ClientArn"]
    if "Certificate" in data:
        out["certificate"] = data["Certificate"]
    if "CertificateFingerprint" in data:
        out["certificate_fingerprint"] = data["CertificateFingerprint"]
    if "LastModifiedTimestamp" in data:
        out["last_modified_timestamp"] = data["LastModifiedTimestamp"]
    if "Label" in data:
        out["label"] = data["Label"]
    return out

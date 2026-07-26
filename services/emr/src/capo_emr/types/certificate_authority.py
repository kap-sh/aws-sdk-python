"""Generated from Smithy shape ``com.amazonaws.emr#CertificateAuthority``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.xml_string


class CertificateAuthority(TypedDict, closed=True):
    certificate_arn: NotRequired["capo_emr.types.xml_string.XmlString"]
    """<p>The Amazon Resource Name (ARN) of the certificate authority in Amazon Web Services Private CA that issued the Spark Connect server certificate.</p>"""
    certificate_data: NotRequired["capo_emr.types.xml_string.XmlString"]
    """<p>The PEM-encoded root CA certificate data. Provide this certificate to your client's trust store when connecting directly to the Spark Connect server over VPC peering.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateAuthority) -> dict:
    out: dict = {}
    if "certificate_arn" in value:
        out["CertificateArn"] = value["certificate_arn"]
    if "certificate_data" in value:
        out["CertificateData"] = value["certificate_data"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CertificateAuthority:
    out: CertificateAuthority = {}  # type: ignore[typeddict-item]
    if "CertificateArn" in data:
        out["certificate_arn"] = data["CertificateArn"]
    if "CertificateData" in data:
        out["certificate_data"] = data["CertificateData"]
    return out

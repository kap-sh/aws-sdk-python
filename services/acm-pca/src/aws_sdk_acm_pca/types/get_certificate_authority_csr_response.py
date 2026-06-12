"""Generated from Smithy shape ``com.amazonaws.acmpca#GetCertificateAuthorityCsrResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_acm_pca.types.csr_body


class GetCertificateAuthorityCsrResponse(TypedDict):
    csr: NotRequired["aws_sdk_acm_pca.types.csr_body.CsrBody"]
    """<p>The base64 PEM-encoded certificate signing request (CSR) for your private CA certificate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCertificateAuthorityCsrResponse) -> dict:
    out: dict = {}
    if "csr" in value:
        out["Csr"] = value["csr"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCertificateAuthorityCsrResponse:
    out: GetCertificateAuthorityCsrResponse = {}  # type: ignore[typeddict-item]
    if "Csr" in data:
        out["csr"] = data["Csr"]
    return out

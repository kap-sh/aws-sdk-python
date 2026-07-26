"""Generated from Smithy shape ``com.amazonaws.acm#DescribeCertificateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.certificate_detail


class DescribeCertificateResponse(TypedDict, closed=True):
    certificate: NotRequired["capo_acm.types.certificate_detail.CertificateDetail"]
    """<p>Metadata about an ACM certificate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCertificateResponse) -> dict:
    out: dict = {}
    if "certificate" in value:
        import capo_acm.types.certificate_detail

        out["Certificate"] = capo_acm.types.certificate_detail.serialize_aws_json_1_1(
            value["certificate"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCertificateResponse:
    out: DescribeCertificateResponse = {}  # type: ignore[typeddict-item]
    if "Certificate" in data:
        import capo_acm.types.certificate_detail

        out["certificate"] = capo_acm.types.certificate_detail.deserialize_aws_json_1_1(
            data["Certificate"]
        )
    return out

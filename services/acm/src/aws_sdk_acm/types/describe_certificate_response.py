"""Generated from Smithy shape ``com.amazonaws.acm#DescribeCertificateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_acm.types.certificate_detail


class DescribeCertificateResponse(TypedDict):
    certificate: NotRequired["aws_sdk_acm.types.certificate_detail.CertificateDetail"]
    """<p>Metadata about an ACM certificate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCertificateResponse) -> dict:
    out: dict = {}
    if "certificate" in value:
        import aws_sdk_acm.types.certificate_detail

        out["Certificate"] = (
            aws_sdk_acm.types.certificate_detail.serialize_aws_json_1_1(
                value["certificate"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCertificateResponse:
    out: DescribeCertificateResponse = {}  # type: ignore[typeddict-item]
    if "Certificate" in data:
        import aws_sdk_acm.types.certificate_detail

        out["certificate"] = (
            aws_sdk_acm.types.certificate_detail.deserialize_aws_json_1_1(
                data["Certificate"]
            )
        )
    return out

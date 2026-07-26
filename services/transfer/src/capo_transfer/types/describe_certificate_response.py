"""Generated from Smithy shape ``com.amazonaws.transfer#DescribeCertificateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transfer.types.described_certificate


class DescribeCertificateResponse(TypedDict, closed=True):
    certificate: "capo_transfer.types.described_certificate.DescribedCertificate"
    """<p>The details for the specified certificate, returned as an object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCertificateResponse) -> dict:
    out: dict = {}
    import capo_transfer.types.described_certificate

    out["Certificate"] = (
        capo_transfer.types.described_certificate.serialize_aws_json_1_1(
            value["certificate"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCertificateResponse:
    out: DescribeCertificateResponse = {}  # type: ignore[typeddict-item]
    if "Certificate" in data:
        import capo_transfer.types.described_certificate

        out["certificate"] = (
            capo_transfer.types.described_certificate.deserialize_aws_json_1_1(
                data["Certificate"]
            )
        )
    else:
        raise DeserializationError("DescribeCertificateResponse.certificate required")
    return out

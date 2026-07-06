"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeCertificateResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.certificate


class DescribeCertificateResult(TypedDict, closed=True):
    certificate: NotRequired["aws_sdk_directory_service.types.certificate.Certificate"]
    """<p>Information about the certificate, including registered date time, certificate state, the reason for the state, expiration date time, and certificate common name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCertificateResult) -> dict:
    out: dict = {}
    if "certificate" in value:
        import aws_sdk_directory_service.types.certificate

        out["Certificate"] = (
            aws_sdk_directory_service.types.certificate.serialize_aws_json_1_1(
                value["certificate"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCertificateResult:
    out: DescribeCertificateResult = {}  # type: ignore[typeddict-item]
    if "Certificate" in data:
        import aws_sdk_directory_service.types.certificate

        out["certificate"] = (
            aws_sdk_directory_service.types.certificate.deserialize_aws_json_1_1(
                data["Certificate"]
            )
        )
    return out

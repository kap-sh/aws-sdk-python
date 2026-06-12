"""Generated from Smithy shape ``com.amazonaws.directoryservice#ListCertificatesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.certificates_info
    import aws_sdk_directory_service.types.next_token


class ListCertificatesResult(TypedDict):
    next_token: NotRequired["aws_sdk_directory_service.types.next_token.NextToken"]
    """<p>Indicates whether another page of certificates is available when the number of available certificates exceeds the page limit.</p>"""
    certificates_info: NotRequired[
        "aws_sdk_directory_service.types.certificates_info.CertificatesInfo"
    ]
    """<p>A list of certificates with basic details including certificate ID, certificate common name, certificate state.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCertificatesResult) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "certificates_info" in value:
        import aws_sdk_directory_service.types.certificates_info

        out["CertificatesInfo"] = (
            aws_sdk_directory_service.types.certificates_info.serialize_aws_json_1_1(
                value["certificates_info"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCertificatesResult:
    out: ListCertificatesResult = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "CertificatesInfo" in data:
        import aws_sdk_directory_service.types.certificates_info

        out["certificates_info"] = (
            aws_sdk_directory_service.types.certificates_info.deserialize_aws_json_1_1(
                data["CertificatesInfo"]
            )
        )
    return out

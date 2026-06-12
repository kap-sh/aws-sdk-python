"""Generated from Smithy shape ``com.amazonaws.transfer#ListCertificatesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.listed_certificates
    import aws_sdk_transfer.types.next_token


class ListCertificatesResponse(TypedDict):
    next_token: NotRequired["aws_sdk_transfer.types.next_token.NextToken"]
    """<p>Returns the next token, which you can use to list the next certificate.</p>"""
    certificates: "aws_sdk_transfer.types.listed_certificates.ListedCertificates"
    """<p>Returns an array of the certificates that are specified in the <code>ListCertificates</code> call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCertificatesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import aws_sdk_transfer.types.listed_certificates

    out["Certificates"] = (
        aws_sdk_transfer.types.listed_certificates.serialize_aws_json_1_1(
            value["certificates"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCertificatesResponse:
    out: ListCertificatesResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Certificates" in data:
        import aws_sdk_transfer.types.listed_certificates

        out["certificates"] = (
            aws_sdk_transfer.types.listed_certificates.deserialize_aws_json_1_1(
                data["Certificates"]
            )
        )
    else:
        raise DeserializationError("ListCertificatesResponse.certificates required")
    return out

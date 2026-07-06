"""Generated from Smithy shape ``com.amazonaws.lightsail#DeleteCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.certificate_name


class DeleteCertificateRequest(TypedDict, closed=True):
    certificate_name: "aws_sdk_lightsail.types.certificate_name.CertificateName"
    """<p>The name of the certificate to delete.</p> <p>Use the <code>GetCertificates</code> action to get a list of certificate names that you can specify.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteCertificateRequest) -> dict:
    out: dict = {}
    out["certificateName"] = value["certificate_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteCertificateRequest:
    out: DeleteCertificateRequest = {}  # type: ignore[typeddict-item]
    if "certificateName" in data:
        out["certificate_name"] = data["certificateName"]
    else:
        raise DeserializationError("DeleteCertificateRequest.certificate_name required")
    return out

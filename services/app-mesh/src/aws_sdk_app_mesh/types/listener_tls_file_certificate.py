"""Generated from Smithy shape ``com.amazonaws.appmesh#ListenerTlsFileCertificate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.file_path


class ListenerTlsFileCertificate(TypedDict, closed=True):
    certificate_chain: "aws_sdk_app_mesh.types.file_path.FilePath"
    """<p>The certificate chain for the certificate.</p>"""
    private_key: "aws_sdk_app_mesh.types.file_path.FilePath"
    """<p>The private key for a certificate stored on the file system of the virtual node that the proxy is running on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListenerTlsFileCertificate) -> dict:
    out: dict = {}
    out["certificateChain"] = value["certificate_chain"]
    out["privateKey"] = value["private_key"]
    return out


def deserialize_json(data: dict) -> ListenerTlsFileCertificate:
    out: ListenerTlsFileCertificate = {}  # type: ignore[typeddict-item]
    if "certificateChain" in data:
        out["certificate_chain"] = data["certificateChain"]
    else:
        raise DeserializationError(
            "ListenerTlsFileCertificate.certificate_chain required"
        )
    if "privateKey" in data:
        out["private_key"] = data["privateKey"]
    else:
        raise DeserializationError("ListenerTlsFileCertificate.private_key required")
    return out

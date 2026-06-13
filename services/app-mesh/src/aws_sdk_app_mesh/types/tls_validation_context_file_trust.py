"""Generated from Smithy shape ``com.amazonaws.appmesh#TlsValidationContextFileTrust``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.file_path


class TlsValidationContextFileTrust(TypedDict):
    certificate_chain: "aws_sdk_app_mesh.types.file_path.FilePath"
    """<p>The certificate trust chain for a certificate stored on the file system of the virtual node that the proxy is running on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TlsValidationContextFileTrust) -> dict:
    out: dict = {}
    out["certificateChain"] = value["certificate_chain"]
    return out


def deserialize_json(data: dict) -> TlsValidationContextFileTrust:
    out: TlsValidationContextFileTrust = {}  # type: ignore[typeddict-item]
    if "certificateChain" in data:
        out["certificate_chain"] = data["certificateChain"]
    else:
        raise DeserializationError(
            "TlsValidationContextFileTrust.certificate_chain required"
        )
    return out

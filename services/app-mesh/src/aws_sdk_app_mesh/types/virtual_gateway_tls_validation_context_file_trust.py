"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualGatewayTlsValidationContextFileTrust``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.file_path


class VirtualGatewayTlsValidationContextFileTrust(TypedDict):
    certificate_chain: "aws_sdk_app_mesh.types.file_path.FilePath"
    """<p>The certificate trust chain for a certificate stored on the file system of the virtual node that the proxy is running on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualGatewayTlsValidationContextFileTrust) -> dict:
    out: dict = {}
    out["certificateChain"] = value["certificate_chain"]
    return out


def deserialize_json(data: dict) -> VirtualGatewayTlsValidationContextFileTrust:
    out: VirtualGatewayTlsValidationContextFileTrust = {}  # type: ignore[typeddict-item]
    if "certificateChain" in data:
        out["certificate_chain"] = data["certificateChain"]
    else:
        raise DeserializationError(
            "VirtualGatewayTlsValidationContextFileTrust.certificate_chain required"
        )
    return out

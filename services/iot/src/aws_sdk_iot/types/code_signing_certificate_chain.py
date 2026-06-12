"""Generated from Smithy shape ``com.amazonaws.iot#CodeSigningCertificateChain``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.certificate_name
    import aws_sdk_iot.types.inline_document


class CodeSigningCertificateChain(TypedDict):
    certificate_name: NotRequired["aws_sdk_iot.types.certificate_name.CertificateName"]
    """<p>The name of the certificate.</p>"""
    inline_document: NotRequired["aws_sdk_iot.types.inline_document.InlineDocument"]
    """<p>A base64 encoded binary representation of the code signing certificate chain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeSigningCertificateChain) -> dict:
    out: dict = {}
    if "certificate_name" in value:
        out["certificateName"] = value["certificate_name"]
    if "inline_document" in value:
        out["inlineDocument"] = value["inline_document"]
    return out


def deserialize_json(data: dict) -> CodeSigningCertificateChain:
    out: CodeSigningCertificateChain = {}  # type: ignore[typeddict-item]
    if "certificateName" in data:
        out["certificate_name"] = data["certificateName"]
    if "inlineDocument" in data:
        out["inline_document"] = data["inlineDocument"]
    return out

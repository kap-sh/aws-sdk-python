"""Generated from Smithy shape ``com.amazonaws.iot#CodeSigningSignature``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.signature


class CodeSigningSignature(TypedDict):
    inline_document: NotRequired["aws_sdk_iot.types.signature.Signature"]
    """<p>A base64 encoded binary representation of the code signing signature.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeSigningSignature) -> dict:
    out: dict = {}
    if "inline_document" in value:
        import aws_sdk_iot.types.signature

        out["inlineDocument"] = aws_sdk_iot.types.signature.serialize_json(
            value["inline_document"]
        )
    return out


def deserialize_json(data: dict) -> CodeSigningSignature:
    out: CodeSigningSignature = {}  # type: ignore[typeddict-item]
    if "inlineDocument" in data:
        import aws_sdk_iot.types.signature

        out["inline_document"] = aws_sdk_iot.types.signature.deserialize_json(
            data["inlineDocument"]
        )
    return out

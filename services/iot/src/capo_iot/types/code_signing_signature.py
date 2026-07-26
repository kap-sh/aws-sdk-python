"""Generated from Smithy shape ``com.amazonaws.iot#CodeSigningSignature``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.signature


class CodeSigningSignature(TypedDict, closed=True):
    inline_document: NotRequired["capo_iot.types.signature.Signature"]
    """<p>A base64 encoded binary representation of the code signing signature.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeSigningSignature) -> dict:
    out: dict = {}
    if "inline_document" in value:
        import capo_iot.types.signature

        out["inlineDocument"] = capo_iot.types.signature.serialize_json(
            value["inline_document"]
        )
    return out


def deserialize_json(data: dict) -> CodeSigningSignature:
    out: CodeSigningSignature = {}  # type: ignore[typeddict-item]
    if "inlineDocument" in data:
        import capo_iot.types.signature

        out["inline_document"] = capo_iot.types.signature.deserialize_json(
            data["inlineDocument"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.signer#SigningImageFormat``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_signer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_signer.types.image_format
    import capo_signer.types.image_formats


class SigningImageFormat(TypedDict, closed=True):
    supported_formats: "capo_signer.types.image_formats.ImageFormats"
    """<p>The supported formats of a signing image.</p>"""
    default_format: "capo_signer.types.image_format.ImageFormat"
    """<p>The default format of a signing image.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SigningImageFormat) -> dict:
    out: dict = {}
    import capo_signer.types.image_formats

    out["supportedFormats"] = capo_signer.types.image_formats.serialize_json(
        value["supported_formats"]
    )
    import capo_signer.types.image_format

    out["defaultFormat"] = capo_signer.types.image_format.serialize_json(
        value["default_format"]
    )
    return out


def deserialize_json(data: dict) -> SigningImageFormat:
    out: SigningImageFormat = {}  # type: ignore[typeddict-item]
    if "supportedFormats" in data:
        import capo_signer.types.image_formats

        out["supported_formats"] = capo_signer.types.image_formats.deserialize_json(
            data["supportedFormats"]
        )
    else:
        raise DeserializationError("SigningImageFormat.supported_formats required")
    if "defaultFormat" in data:
        import capo_signer.types.image_format

        out["default_format"] = capo_signer.types.image_format.deserialize_json(
            data["defaultFormat"]
        )
    else:
        raise DeserializationError("SigningImageFormat.default_format required")
    return out

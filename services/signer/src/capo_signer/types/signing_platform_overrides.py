"""Generated from Smithy shape ``com.amazonaws.signer#SigningPlatformOverrides``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_signer.types.image_format
    import capo_signer.types.signing_configuration_overrides


class SigningPlatformOverrides(TypedDict, closed=True):
    signing_configuration: NotRequired[
        "capo_signer.types.signing_configuration_overrides.SigningConfigurationOverrides"
    ]
    """<p>A signing configuration that overrides the default encryption or hash algorithm of a signing job.</p>"""
    signing_image_format: NotRequired["capo_signer.types.image_format.ImageFormat"]
    """<p>A signed image is a JSON object. When overriding the default signing platform configuration, a customer can select either of two signing formats, <code>JSONEmbedded</code> or <code>JSONDetached</code>. (A third format value, <code>JSON</code>, is reserved for future use.) With <code>JSONEmbedded</code>, the signing image has the payload embedded in it. With <code>JSONDetached</code>, the payload is not be embedded in the signing image.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SigningPlatformOverrides) -> dict:
    out: dict = {}
    if "signing_configuration" in value:
        import capo_signer.types.signing_configuration_overrides

        out["signingConfiguration"] = (
            capo_signer.types.signing_configuration_overrides.serialize_json(
                value["signing_configuration"]
            )
        )
    if "signing_image_format" in value:
        import capo_signer.types.image_format

        out["signingImageFormat"] = capo_signer.types.image_format.serialize_json(
            value["signing_image_format"]
        )
    return out


def deserialize_json(data: dict) -> SigningPlatformOverrides:
    out: SigningPlatformOverrides = {}  # type: ignore[typeddict-item]
    if "signingConfiguration" in data:
        import capo_signer.types.signing_configuration_overrides

        out["signing_configuration"] = (
            capo_signer.types.signing_configuration_overrides.deserialize_json(
                data["signingConfiguration"]
            )
        )
    if "signingImageFormat" in data:
        import capo_signer.types.image_format

        out["signing_image_format"] = capo_signer.types.image_format.deserialize_json(
            data["signingImageFormat"]
        )
    return out

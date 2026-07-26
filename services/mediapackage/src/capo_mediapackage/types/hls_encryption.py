"""Generated from Smithy shape ``com.amazonaws.mediapackage#HlsEncryption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackage.types.__boolean
    import capo_mediapackage.types.__integer
    import capo_mediapackage.types.__string
    import capo_mediapackage.types.encryption_method
    import capo_mediapackage.types.speke_key_provider


class HlsEncryption(TypedDict, closed=True):
    constant_initialization_vector: NotRequired[
        "capo_mediapackage.types.__string.__string"
    ]
    """A constant initialization vector for encryption (optional). When not specified the initialization vector will be periodically rotated."""
    encryption_method: NotRequired[
        "capo_mediapackage.types.encryption_method.EncryptionMethod"
    ]
    """The encryption method to use."""
    key_rotation_interval_seconds: NotRequired[
        "capo_mediapackage.types.__integer.__integer"
    ]
    """Interval (in seconds) between each encryption key rotation."""
    repeat_ext_x_key: NotRequired["capo_mediapackage.types.__boolean.__boolean"]
    """When enabled, the EXT-X-KEY tag will be repeated in output manifests."""
    speke_key_provider: NotRequired[
        "capo_mediapackage.types.speke_key_provider.SpekeKeyProvider"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: HlsEncryption) -> dict:
    out: dict = {}
    if "constant_initialization_vector" in value:
        out["constantInitializationVector"] = value["constant_initialization_vector"]
    if "encryption_method" in value:
        import capo_mediapackage.types.encryption_method

        out["encryptionMethod"] = (
            capo_mediapackage.types.encryption_method.serialize_json(
                value["encryption_method"]
            )
        )
    if "key_rotation_interval_seconds" in value:
        out["keyRotationIntervalSeconds"] = value["key_rotation_interval_seconds"]
    if "repeat_ext_x_key" in value:
        out["repeatExtXKey"] = value["repeat_ext_x_key"]
    if "speke_key_provider" in value:
        import capo_mediapackage.types.speke_key_provider

        out["spekeKeyProvider"] = (
            capo_mediapackage.types.speke_key_provider.serialize_json(
                value["speke_key_provider"]
            )
        )
    return out


def deserialize_json(data: dict) -> HlsEncryption:
    out: HlsEncryption = {}  # type: ignore[typeddict-item]
    if "constantInitializationVector" in data:
        out["constant_initialization_vector"] = data["constantInitializationVector"]
    if "encryptionMethod" in data:
        import capo_mediapackage.types.encryption_method

        out["encryption_method"] = (
            capo_mediapackage.types.encryption_method.deserialize_json(
                data["encryptionMethod"]
            )
        )
    if "keyRotationIntervalSeconds" in data:
        out["key_rotation_interval_seconds"] = data["keyRotationIntervalSeconds"]
    if "repeatExtXKey" in data:
        out["repeat_ext_x_key"] = data["repeatExtXKey"]
    if "spekeKeyProvider" in data:
        import capo_mediapackage.types.speke_key_provider

        out["speke_key_provider"] = (
            capo_mediapackage.types.speke_key_provider.deserialize_json(
                data["spekeKeyProvider"]
            )
        )
    return out

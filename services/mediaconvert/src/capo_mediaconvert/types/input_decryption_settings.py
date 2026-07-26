"""Generated from Smithy shape ``com.amazonaws.mediaconvert#InputDecryptionSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__string_min9_max19_pattern_az26_east_west_central_north_south_east_west1912
    import capo_mediaconvert.types.__string_min16_max24_pattern_a_za_z0922_a_za_z0916
    import capo_mediaconvert.types.__string_min24_max512_pattern_a_za_z0902
    import capo_mediaconvert.types.decryption_mode


class InputDecryptionSettings(TypedDict, closed=True):
    decryption_mode: NotRequired[
        "capo_mediaconvert.types.decryption_mode.DecryptionMode"
    ]
    """Specify the encryption mode that you used to encrypt your input files."""
    encrypted_decryption_key: NotRequired[
        "capo_mediaconvert.types.__string_min24_max512_pattern_a_za_z0902.__stringMin24Max512PatternAZaZ0902"
    ]
    """Warning! Don't provide your encryption key in plaintext. Your job settings could be intercepted, making your encrypted content vulnerable. Specify the encrypted version of the data key that you used to encrypt your content. The data key must be encrypted by AWS Key Management Service (KMS). The key can be 128, 192, or 256 bits."""
    initialization_vector: NotRequired[
        "capo_mediaconvert.types.__string_min16_max24_pattern_a_za_z0922_a_za_z0916.__stringMin16Max24PatternAZaZ0922AZaZ0916"
    ]
    """Specify the initialization vector that you used when you encrypted your content before uploading it to Amazon S3. You can use a 16-byte initialization vector with any encryption mode. Or, you can use a 12-byte initialization vector with GCM or CTR. MediaConvert accepts only initialization vectors that are base64-encoded."""
    kms_key_region: NotRequired[
        "capo_mediaconvert.types.__string_min9_max19_pattern_az26_east_west_central_north_south_east_west1912.__stringMin9Max19PatternAZ26EastWestCentralNorthSouthEastWest1912"
    ]
    """Specify the AWS Region for AWS Key Management Service (KMS) that you used to encrypt your data key, if that Region is different from the one you are using for AWS Elemental MediaConvert."""


# --- restJson1 ser/de ---
def serialize_json(value: InputDecryptionSettings) -> dict:
    out: dict = {}
    if "decryption_mode" in value:
        import capo_mediaconvert.types.decryption_mode

        out["decryptionMode"] = capo_mediaconvert.types.decryption_mode.serialize_json(
            value["decryption_mode"]
        )
    if "encrypted_decryption_key" in value:
        out["encryptedDecryptionKey"] = value["encrypted_decryption_key"]
    if "initialization_vector" in value:
        out["initializationVector"] = value["initialization_vector"]
    if "kms_key_region" in value:
        out["kmsKeyRegion"] = value["kms_key_region"]
    return out


def deserialize_json(data: dict) -> InputDecryptionSettings:
    out: InputDecryptionSettings = {}  # type: ignore[typeddict-item]
    if "decryptionMode" in data:
        import capo_mediaconvert.types.decryption_mode

        out["decryption_mode"] = (
            capo_mediaconvert.types.decryption_mode.deserialize_json(
                data["decryptionMode"]
            )
        )
    if "encryptedDecryptionKey" in data:
        out["encrypted_decryption_key"] = data["encryptedDecryptionKey"]
    if "initializationVector" in data:
        out["initialization_vector"] = data["initializationVector"]
    if "kmsKeyRegion" in data:
        out["kms_key_region"] = data["kmsKeyRegion"]
    return out

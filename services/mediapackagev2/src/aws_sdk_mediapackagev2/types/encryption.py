"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#Encryption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mediapackagev2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.encryption_method
    import aws_sdk_mediapackagev2.types.speke_key_provider


class Encryption(TypedDict, closed=True):
    constant_initialization_vector: NotRequired["str"]
    """<p>A 128-bit, 16-byte hex value represented by a 32-character string, used in conjunction with the key for encrypting content. If you don't specify a value, then MediaPackage creates the constant initialization vector (IV).</p>"""
    encryption_method: "aws_sdk_mediapackagev2.types.encryption_method.EncryptionMethod"
    """<p>The encryption method to use.</p>"""
    key_rotation_interval_seconds: NotRequired["int"]
    """<p>The frequency (in seconds) of key changes for live workflows, in which content is streamed real time. The service retrieves content keys before the live content begins streaming, and then retrieves them as needed over the lifetime of the workflow. By default, key rotation is set to 300 seconds (5 minutes), the minimum rotation interval, which is equivalent to setting it to 300. If you don't enter an interval, content keys aren't rotated.</p> <p>The following example setting causes the service to rotate keys every thirty minutes: <code>1800</code> </p>"""
    cmaf_exclude_segment_drm_metadata: NotRequired["bool"]
    """<p>Excludes SEIG and SGPD boxes from segment metadata in CMAF containers.</p> <p>When set to <code>true</code>, MediaPackage omits these DRM metadata boxes from CMAF segments, which can improve compatibility with certain devices and players that don't support these boxes.</p> <p>Important considerations:</p> <ul> <li> <p>This setting only affects CMAF container formats</p> </li> <li> <p>Key rotation can still be handled through media playlist signaling</p> </li> <li> <p>PSSH and TENC boxes remain unaffected</p> </li> <li> <p>Default behavior is preserved when this setting is disabled</p> </li> </ul> <p>Valid values: <code>true</code> | <code>false</code> </p> <p>Default: <code>false</code> </p>"""
    speke_key_provider: (
        "aws_sdk_mediapackagev2.types.speke_key_provider.SpekeKeyProvider"
    )
    """<p>The parameters for the SPEKE key provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Encryption) -> dict:
    out: dict = {}
    if "constant_initialization_vector" in value:
        out["ConstantInitializationVector"] = value["constant_initialization_vector"]
    import aws_sdk_mediapackagev2.types.encryption_method

    out["EncryptionMethod"] = (
        aws_sdk_mediapackagev2.types.encryption_method.serialize_json(
            value["encryption_method"]
        )
    )
    if "key_rotation_interval_seconds" in value:
        out["KeyRotationIntervalSeconds"] = value["key_rotation_interval_seconds"]
    if "cmaf_exclude_segment_drm_metadata" in value:
        out["CmafExcludeSegmentDrmMetadata"] = value[
            "cmaf_exclude_segment_drm_metadata"
        ]
    import aws_sdk_mediapackagev2.types.speke_key_provider

    out["SpekeKeyProvider"] = (
        aws_sdk_mediapackagev2.types.speke_key_provider.serialize_json(
            value["speke_key_provider"]
        )
    )
    return out


def deserialize_json(data: dict) -> Encryption:
    out: Encryption = {}  # type: ignore[typeddict-item]
    if "ConstantInitializationVector" in data:
        out["constant_initialization_vector"] = data["ConstantInitializationVector"]
    if "EncryptionMethod" in data:
        import aws_sdk_mediapackagev2.types.encryption_method

        out["encryption_method"] = (
            aws_sdk_mediapackagev2.types.encryption_method.deserialize_json(
                data["EncryptionMethod"]
            )
        )
    else:
        raise DeserializationError("Encryption.encryption_method required")
    if "KeyRotationIntervalSeconds" in data:
        out["key_rotation_interval_seconds"] = data["KeyRotationIntervalSeconds"]
    if "CmafExcludeSegmentDrmMetadata" in data:
        out["cmaf_exclude_segment_drm_metadata"] = data["CmafExcludeSegmentDrmMetadata"]
    if "SpekeKeyProvider" in data:
        import aws_sdk_mediapackagev2.types.speke_key_provider

        out["speke_key_provider"] = (
            aws_sdk_mediapackagev2.types.speke_key_provider.deserialize_json(
                data["SpekeKeyProvider"]
            )
        )
    else:
        raise DeserializationError("Encryption.speke_key_provider required")
    return out

"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#PlayReadyDrm``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.key_id_guid
    import aws_sdk_elastic_transcoder.types.non_empty_base64_encoded_string
    import aws_sdk_elastic_transcoder.types.one_to512_string
    import aws_sdk_elastic_transcoder.types.play_ready_drm_format_string
    import aws_sdk_elastic_transcoder.types.zero_to255_string


class PlayReadyDrm(TypedDict, closed=True):
    format: NotRequired[
        "aws_sdk_elastic_transcoder.types.play_ready_drm_format_string.PlayReadyDrmFormatString"
    ]
    """<p>The type of DRM, if any, that you want Elastic Transcoder to apply to the output files associated with this playlist.</p>"""
    key: NotRequired[
        "aws_sdk_elastic_transcoder.types.non_empty_base64_encoded_string.NonEmptyBase64EncodedString"
    ]
    """<p>The DRM key for your file, provided by your DRM license provider. The key must be base64-encoded, and it must be one of the following bit lengths before being base64-encoded:</p> <p> <code>128</code>, <code>192</code>, or <code>256</code>. </p> <p>The key must also be encrypted by using AWS KMS.</p>"""
    key_md5: NotRequired[
        "aws_sdk_elastic_transcoder.types.non_empty_base64_encoded_string.NonEmptyBase64EncodedString"
    ]
    """<p>The MD5 digest of the key used for DRM on your file, and that you want Elastic Transcoder to use as a checksum to make sure your key was not corrupted in transit. The key MD5 must be base64-encoded, and it must be exactly 16 bytes before being base64-encoded.</p>"""
    key_id: NotRequired["aws_sdk_elastic_transcoder.types.key_id_guid.KeyIdGuid"]
    """<p>The ID for your DRM key, so that your DRM license provider knows which key to provide.</p> <p>The key ID must be provided in big endian, and Elastic Transcoder converts it to little endian before inserting it into the PlayReady DRM headers. If you are unsure whether your license server provides your key ID in big or little endian, check with your DRM provider.</p>"""
    initialization_vector: NotRequired[
        "aws_sdk_elastic_transcoder.types.zero_to255_string.ZeroTo255String"
    ]
    """<p>The series of random bits created by a random bit generator, unique for every encryption operation, that you want Elastic Transcoder to use to encrypt your files. The initialization vector must be base64-encoded, and it must be exactly 8 bytes long before being base64-encoded. If no initialization vector is provided, Elastic Transcoder generates one for you.</p>"""
    license_acquisition_url: NotRequired[
        "aws_sdk_elastic_transcoder.types.one_to512_string.OneTo512String"
    ]
    """<p>The location of the license key required to play DRM content. The URL must be an absolute path, and is referenced by the PlayReady header. The PlayReady header is referenced in the protection header of the client manifest for Smooth Streaming outputs, and in the EXT-X-DXDRM and EXT-XDXDRMINFO metadata tags for HLS playlist outputs. An example URL looks like this: <code>https://www.example.com/exampleKey/</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PlayReadyDrm) -> dict:
    out: dict = {}
    if "format" in value:
        out["Format"] = value["format"]
    if "key" in value:
        out["Key"] = value["key"]
    if "key_md5" in value:
        out["KeyMd5"] = value["key_md5"]
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    if "initialization_vector" in value:
        out["InitializationVector"] = value["initialization_vector"]
    if "license_acquisition_url" in value:
        out["LicenseAcquisitionUrl"] = value["license_acquisition_url"]
    return out


def deserialize_json(data: dict) -> PlayReadyDrm:
    out: PlayReadyDrm = {}  # type: ignore[typeddict-item]
    if "Format" in data:
        out["format"] = data["Format"]
    if "Key" in data:
        out["key"] = data["Key"]
    if "KeyMd5" in data:
        out["key_md5"] = data["KeyMd5"]
    if "KeyId" in data:
        out["key_id"] = data["KeyId"]
    if "InitializationVector" in data:
        out["initialization_vector"] = data["InitializationVector"]
    if "LicenseAcquisitionUrl" in data:
        out["license_acquisition_url"] = data["LicenseAcquisitionUrl"]
    return out

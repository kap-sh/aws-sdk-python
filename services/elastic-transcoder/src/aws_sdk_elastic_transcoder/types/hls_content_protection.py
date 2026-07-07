"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#HlsContentProtection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.base64_encoded_string
    import aws_sdk_elastic_transcoder.types.hls_content_protection_method
    import aws_sdk_elastic_transcoder.types.key_storage_policy
    import aws_sdk_elastic_transcoder.types.zero_to255_string
    import aws_sdk_elastic_transcoder.types.zero_to512_string


class HlsContentProtection(TypedDict, closed=True):
    method: NotRequired[
        "aws_sdk_elastic_transcoder.types.hls_content_protection_method.HlsContentProtectionMethod"
    ]
    """<p>The content protection method for your output. The only valid value is: <code>aes-128</code>.</p> <p>This value is written into the method attribute of the <code>EXT-X-KEY</code> metadata tag in the output playlist.</p>"""
    key: NotRequired[
        "aws_sdk_elastic_transcoder.types.base64_encoded_string.Base64EncodedString"
    ]
    """<p>If you want Elastic Transcoder to generate a key for you, leave this field blank.</p> <p>If you choose to supply your own key, you must encrypt the key by using AWS KMS. The key must be base64-encoded, and it must be one of the following bit lengths before being base64-encoded:</p> <p> <code>128</code>, <code>192</code>, or <code>256</code>. </p>"""
    key_md5: NotRequired[
        "aws_sdk_elastic_transcoder.types.base64_encoded_string.Base64EncodedString"
    ]
    """<p>If Elastic Transcoder is generating your key for you, you must leave this field blank.</p> <p>The MD5 digest of the key that you want Elastic Transcoder to use to encrypt your output file, and that you want Elastic Transcoder to use as a checksum to make sure your key was not corrupted in transit. The key MD5 must be base64-encoded, and it must be exactly 16 bytes before being base64- encoded.</p>"""
    initialization_vector: NotRequired[
        "aws_sdk_elastic_transcoder.types.zero_to255_string.ZeroTo255String"
    ]
    """<p>If Elastic Transcoder is generating your key for you, you must leave this field blank.</p> <p>The series of random bits created by a random bit generator, unique for every encryption operation, that you want Elastic Transcoder to use to encrypt your output files. The initialization vector must be base64-encoded, and it must be exactly 16 bytes before being base64-encoded.</p>"""
    license_acquisition_url: NotRequired[
        "aws_sdk_elastic_transcoder.types.zero_to512_string.ZeroTo512String"
    ]
    """<p>The location of the license key required to decrypt your HLS playlist. The URL must be an absolute path, and is referenced in the URI attribute of the EXT-X-KEY metadata tag in the playlist file.</p>"""
    key_storage_policy: NotRequired[
        "aws_sdk_elastic_transcoder.types.key_storage_policy.KeyStoragePolicy"
    ]
    """<p>Specify whether you want Elastic Transcoder to write your HLS license key to an Amazon S3 bucket. If you choose <code>WithVariantPlaylists</code>, <code>LicenseAcquisitionUrl</code> must be left blank and Elastic Transcoder writes your data key into the same bucket as the associated playlist.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HlsContentProtection) -> dict:
    out: dict = {}
    if "method" in value:
        out["Method"] = value["method"]
    if "key" in value:
        out["Key"] = value["key"]
    if "key_md5" in value:
        out["KeyMd5"] = value["key_md5"]
    if "initialization_vector" in value:
        out["InitializationVector"] = value["initialization_vector"]
    if "license_acquisition_url" in value:
        out["LicenseAcquisitionUrl"] = value["license_acquisition_url"]
    if "key_storage_policy" in value:
        out["KeyStoragePolicy"] = value["key_storage_policy"]
    return out


def deserialize_json(data: dict) -> HlsContentProtection:
    out: HlsContentProtection = {}  # type: ignore[typeddict-item]
    if "Method" in data:
        out["method"] = data["Method"]
    if "Key" in data:
        out["key"] = data["Key"]
    if "KeyMd5" in data:
        out["key_md5"] = data["KeyMd5"]
    if "InitializationVector" in data:
        out["initialization_vector"] = data["InitializationVector"]
    if "LicenseAcquisitionUrl" in data:
        out["license_acquisition_url"] = data["LicenseAcquisitionUrl"]
    if "KeyStoragePolicy" in data:
        out["key_storage_policy"] = data["KeyStoragePolicy"]
    return out

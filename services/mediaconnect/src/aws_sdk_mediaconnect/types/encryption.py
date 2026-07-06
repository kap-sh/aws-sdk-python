"""Generated from Smithy shape ``com.amazonaws.mediaconnect#Encryption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.algorithm
    import aws_sdk_mediaconnect.types.key_type


class Encryption(TypedDict, closed=True):
    algorithm: NotRequired["aws_sdk_mediaconnect.types.algorithm.Algorithm"]
    """<p> The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).</p>"""
    constant_initialization_vector: NotRequired["str"]
    """<p> A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.</p>"""
    device_id: NotRequired["str"]
    """<p> The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.</p>"""
    key_type: NotRequired["aws_sdk_mediaconnect.types.key_type.KeyType"]
    """<p> The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).</p>"""
    region: NotRequired["str"]
    """<p> The Amazon Web Services Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.</p>"""
    resource_id: NotRequired["str"]
    """<p> An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.</p>"""
    role_arn: NotRequired["str"]
    """<p> The ARN of the role that you created during setup (when you set up MediaConnect as a trusted entity).</p>"""
    secret_arn: NotRequired["str"]
    """<p> The ARN of the secret that you created in Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.</p>"""
    url: NotRequired["str"]
    """<p> The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Encryption) -> dict:
    out: dict = {}
    if "algorithm" in value:
        import aws_sdk_mediaconnect.types.algorithm

        out["algorithm"] = aws_sdk_mediaconnect.types.algorithm.serialize_json(
            value["algorithm"]
        )
    if "constant_initialization_vector" in value:
        out["constantInitializationVector"] = value["constant_initialization_vector"]
    if "device_id" in value:
        out["deviceId"] = value["device_id"]
    if "key_type" in value:
        import aws_sdk_mediaconnect.types.key_type

        out["keyType"] = aws_sdk_mediaconnect.types.key_type.serialize_json(
            value["key_type"]
        )
    if "region" in value:
        out["region"] = value["region"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "secret_arn" in value:
        out["secretArn"] = value["secret_arn"]
    if "url" in value:
        out["url"] = value["url"]
    return out


def deserialize_json(data: dict) -> Encryption:
    out: Encryption = {}  # type: ignore[typeddict-item]
    if "algorithm" in data:
        import aws_sdk_mediaconnect.types.algorithm

        out["algorithm"] = aws_sdk_mediaconnect.types.algorithm.deserialize_json(
            data["algorithm"]
        )
    if "constantInitializationVector" in data:
        out["constant_initialization_vector"] = data["constantInitializationVector"]
    if "deviceId" in data:
        out["device_id"] = data["deviceId"]
    if "keyType" in data:
        import aws_sdk_mediaconnect.types.key_type

        out["key_type"] = aws_sdk_mediaconnect.types.key_type.deserialize_json(
            data["keyType"]
        )
    if "region" in data:
        out["region"] = data["region"]
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "secretArn" in data:
        out["secret_arn"] = data["secretArn"]
    if "url" in data:
        out["url"] = data["url"]
    return out

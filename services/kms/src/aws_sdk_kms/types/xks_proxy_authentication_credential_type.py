"""Generated from Smithy shape ``com.amazonaws.kms#XksProxyAuthenticationCredentialType``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kms.types.xks_proxy_authentication_access_key_id_type
    import aws_sdk_kms.types.xks_proxy_authentication_raw_secret_access_key_type


class XksProxyAuthenticationCredentialType(TypedDict):
    access_key_id: "aws_sdk_kms.types.xks_proxy_authentication_access_key_id_type.XksProxyAuthenticationAccessKeyIdType"
    """<p>A unique identifier for the raw secret access key.</p>"""
    raw_secret_access_key: "aws_sdk_kms.types.xks_proxy_authentication_raw_secret_access_key_type.XksProxyAuthenticationRawSecretAccessKeyType"
    """<p>A secret string of 43-64 characters. Valid characters are a-z, A-Z, 0-9, /, +, and =.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: XksProxyAuthenticationCredentialType) -> dict:
    out: dict = {}
    out["AccessKeyId"] = value["access_key_id"]
    out["RawSecretAccessKey"] = value["raw_secret_access_key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> XksProxyAuthenticationCredentialType:
    out: XksProxyAuthenticationCredentialType = {}  # type: ignore[typeddict-item]
    if "AccessKeyId" in data:
        out["access_key_id"] = data["AccessKeyId"]
    else:
        raise DeserializationError(
            "XksProxyAuthenticationCredentialType.access_key_id required"
        )
    if "RawSecretAccessKey" in data:
        out["raw_secret_access_key"] = data["RawSecretAccessKey"]
    else:
        raise DeserializationError(
            "XksProxyAuthenticationCredentialType.raw_secret_access_key required"
        )
    return out

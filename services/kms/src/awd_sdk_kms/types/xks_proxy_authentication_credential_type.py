"""Generated from Smithy shape ``com.amazonaws.kms#XksProxyAuthenticationCredentialType``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import awd_sdk_kms.types.xks_proxy_authentication_access_key_id_type
    import awd_sdk_kms.types.xks_proxy_authentication_raw_secret_access_key_type


class XksProxyAuthenticationCredentialType(TypedDict):
    access_key_id: "awd_sdk_kms.types.xks_proxy_authentication_access_key_id_type.XksProxyAuthenticationAccessKeyIdType"
    """<p>A unique identifier for the raw secret access key.</p>"""
    raw_secret_access_key: "awd_sdk_kms.types.xks_proxy_authentication_raw_secret_access_key_type.XksProxyAuthenticationRawSecretAccessKeyType"
    """<p>A secret string of 43-64 characters. Valid characters are a-z, A-Z, 0-9, /, +, and =.</p>"""

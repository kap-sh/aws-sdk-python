"""Generated from Smithy shape ``com.amazonaws.odb#OkvEncryptionKeyConfiguration``."""

from typing_extensions import NotRequired, TypedDict

from aws_sdk_odb.errors import DeserializationError


class OkvEncryptionKeyConfiguration(TypedDict, closed=True):
    certificate_directory_name: "str"
    """<p>The name of the directory that contains the Oracle Key Vault (OKV) certificate.</p>"""
    certificate_id: NotRequired["str"]
    """<p>The identifier of the Oracle Key Vault (OKV) certificate.</p>"""
    directory_name: "str"
    """<p>The name of the directory where the Oracle Key Vault (OKV) configuration is stored.</p>"""
    okv_kms_key: "str"
    """<p>The identifier of the Oracle Key Vault (OKV) key to use for encryption.</p>"""
    okv_uri: "str"
    """<p>The URI of the Oracle Key Vault (OKV) server.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OkvEncryptionKeyConfiguration) -> dict:
    out: dict = {}
    out["certificateDirectoryName"] = value["certificate_directory_name"]
    if "certificate_id" in value:
        out["certificateId"] = value["certificate_id"]
    out["directoryName"] = value["directory_name"]
    out["okvKmsKey"] = value["okv_kms_key"]
    out["okvUri"] = value["okv_uri"]
    return out


def deserialize_aws_json_1_0(data: dict) -> OkvEncryptionKeyConfiguration:
    out: OkvEncryptionKeyConfiguration = {}  # type: ignore[typeddict-item]
    if "certificateDirectoryName" in data:
        out["certificate_directory_name"] = data["certificateDirectoryName"]
    else:
        raise DeserializationError(
            "OkvEncryptionKeyConfiguration.certificate_directory_name required"
        )
    if "certificateId" in data:
        out["certificate_id"] = data["certificateId"]
    if "directoryName" in data:
        out["directory_name"] = data["directoryName"]
    else:
        raise DeserializationError(
            "OkvEncryptionKeyConfiguration.directory_name required"
        )
    if "okvKmsKey" in data:
        out["okv_kms_key"] = data["okvKmsKey"]
    else:
        raise DeserializationError("OkvEncryptionKeyConfiguration.okv_kms_key required")
    if "okvUri" in data:
        out["okv_uri"] = data["okvUri"]
    else:
        raise DeserializationError("OkvEncryptionKeyConfiguration.okv_uri required")
    return out

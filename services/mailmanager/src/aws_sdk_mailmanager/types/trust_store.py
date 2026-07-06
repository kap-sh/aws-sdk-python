"""Generated from Smithy shape ``com.amazonaws.mailmanager#TrustStore``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.ca_content
    import aws_sdk_mailmanager.types.crl_content
    import aws_sdk_mailmanager.types.kms_key_arn


class TrustStore(TypedDict, closed=True):
    ca_content: "aws_sdk_mailmanager.types.ca_content.CAContent"
    """<p>The PEM-encoded certificate authority (CA) certificates bundle for the trust store.</p>"""
    crl_content: NotRequired["aws_sdk_mailmanager.types.crl_content.CrlContent"]
    """<p>The PEM-encoded certificate revocation lists (CRLs) for the trust store. There can be one CRL per certificate authority (CA) in the trust store.</p>"""
    kms_key_arn: NotRequired["aws_sdk_mailmanager.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key used to encrypt the trust store contents.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TrustStore) -> dict:
    out: dict = {}
    out["CAContent"] = value["ca_content"]
    if "crl_content" in value:
        out["CrlContent"] = value["crl_content"]
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TrustStore:
    out: TrustStore = {}  # type: ignore[typeddict-item]
    if "CAContent" in data:
        out["ca_content"] = data["CAContent"]
    else:
        raise DeserializationError("TrustStore.ca_content required")
    if "CrlContent" in data:
        out["crl_content"] = data["CrlContent"]
    if "KmsKeyArn" in data:
        out["kms_key_arn"] = data["KmsKeyArn"]
    return out

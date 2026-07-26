"""Generated from Smithy shape ``com.amazonaws.healthlake#S3Configuration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_healthlake.errors import DeserializationError

if TYPE_CHECKING:
    import capo_healthlake.types.encryption_key_id
    import capo_healthlake.types.s3_uri


class S3Configuration(TypedDict, closed=True):
    s3_uri: "capo_healthlake.types.s3_uri.S3Uri"
    """<p>The <code>S3Uri</code> is the user-specified S3 location of the FHIR data to be imported into AWS HealthLake.</p>"""
    kms_key_id: "capo_healthlake.types.encryption_key_id.EncryptionKeyID"
    """<p>The Key Management Service (KMS) key ID used to access the S3 bucket. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: S3Configuration) -> dict:
    out: dict = {}
    out["S3Uri"] = value["s3_uri"]
    out["KmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> S3Configuration:
    out: S3Configuration = {}  # type: ignore[typeddict-item]
    if "S3Uri" in data:
        out["s3_uri"] = data["S3Uri"]
    else:
        raise DeserializationError("S3Configuration.s3_uri required")
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    else:
        raise DeserializationError("S3Configuration.kms_key_id required")
    return out

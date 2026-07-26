"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelPackageSecurityConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.kms_key_id


class ModelPackageSecurityConfig(TypedDict, closed=True):
    kms_key_id: NotRequired["capo_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p>The KMS Key ID (<code>KMSKeyId</code>) used for encryption of model package information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelPackageSecurityConfig) -> dict:
    out: dict = {}
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelPackageSecurityConfig:
    out: ModelPackageSecurityConfig = {}  # type: ignore[typeddict-item]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    return out

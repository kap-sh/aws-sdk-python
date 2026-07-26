"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringOutputConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.kms_key_id
    import capo_sagemaker.types.monitoring_outputs


class MonitoringOutputConfig(TypedDict, closed=True):
    monitoring_outputs: NotRequired[
        "capo_sagemaker.types.monitoring_outputs.MonitoringOutputs"
    ]
    """<p>Monitoring outputs for monitoring jobs. This is where the output of the periodic monitoring jobs is uploaded.</p>"""
    kms_key_id: NotRequired["capo_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p>The Key Management Service (KMS) key that Amazon SageMaker AI uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringOutputConfig) -> dict:
    out: dict = {}
    if "monitoring_outputs" in value:
        import capo_sagemaker.types.monitoring_outputs

        out["MonitoringOutputs"] = (
            capo_sagemaker.types.monitoring_outputs.serialize_aws_json_1_1(
                value["monitoring_outputs"]
            )
        )
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MonitoringOutputConfig:
    out: MonitoringOutputConfig = {}  # type: ignore[typeddict-item]
    if "MonitoringOutputs" in data:
        import capo_sagemaker.types.monitoring_outputs

        out["monitoring_outputs"] = (
            capo_sagemaker.types.monitoring_outputs.deserialize_aws_json_1_1(
                data["MonitoringOutputs"]
            )
        )
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    return out

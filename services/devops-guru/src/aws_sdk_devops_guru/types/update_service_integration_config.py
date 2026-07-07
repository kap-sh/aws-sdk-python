"""Generated from Smithy shape ``com.amazonaws.devopsguru#UpdateServiceIntegrationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.kms_server_side_encryption_integration_config
    import aws_sdk_devops_guru.types.logs_anomaly_detection_integration_config
    import aws_sdk_devops_guru.types.ops_center_integration_config


class UpdateServiceIntegrationConfig(TypedDict, closed=True):
    ops_center: NotRequired[
        "aws_sdk_devops_guru.types.ops_center_integration_config.OpsCenterIntegrationConfig"
    ]
    logs_anomaly_detection: NotRequired[
        "aws_sdk_devops_guru.types.logs_anomaly_detection_integration_config.LogsAnomalyDetectionIntegrationConfig"
    ]
    """<p> Information about whether DevOps Guru is configured to perform log anomaly detection on Amazon CloudWatch log groups. </p>"""
    kms_server_side_encryption: NotRequired[
        "aws_sdk_devops_guru.types.kms_server_side_encryption_integration_config.KMSServerSideEncryptionIntegrationConfig"
    ]
    """<p> Information about whether DevOps Guru is configured to encrypt server-side data using KMS. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateServiceIntegrationConfig) -> dict:
    out: dict = {}
    if "ops_center" in value:
        import aws_sdk_devops_guru.types.ops_center_integration_config

        out["OpsCenter"] = (
            aws_sdk_devops_guru.types.ops_center_integration_config.serialize_json(
                value["ops_center"]
            )
        )
    if "logs_anomaly_detection" in value:
        import aws_sdk_devops_guru.types.logs_anomaly_detection_integration_config

        out["LogsAnomalyDetection"] = (
            aws_sdk_devops_guru.types.logs_anomaly_detection_integration_config.serialize_json(
                value["logs_anomaly_detection"]
            )
        )
    if "kms_server_side_encryption" in value:
        import aws_sdk_devops_guru.types.kms_server_side_encryption_integration_config

        out["KMSServerSideEncryption"] = (
            aws_sdk_devops_guru.types.kms_server_side_encryption_integration_config.serialize_json(
                value["kms_server_side_encryption"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateServiceIntegrationConfig:
    out: UpdateServiceIntegrationConfig = {}  # type: ignore[typeddict-item]
    if "OpsCenter" in data:
        import aws_sdk_devops_guru.types.ops_center_integration_config

        out["ops_center"] = (
            aws_sdk_devops_guru.types.ops_center_integration_config.deserialize_json(
                data["OpsCenter"]
            )
        )
    if "LogsAnomalyDetection" in data:
        import aws_sdk_devops_guru.types.logs_anomaly_detection_integration_config

        out["logs_anomaly_detection"] = (
            aws_sdk_devops_guru.types.logs_anomaly_detection_integration_config.deserialize_json(
                data["LogsAnomalyDetection"]
            )
        )
    if "KMSServerSideEncryption" in data:
        import aws_sdk_devops_guru.types.kms_server_side_encryption_integration_config

        out["kms_server_side_encryption"] = (
            aws_sdk_devops_guru.types.kms_server_side_encryption_integration_config.deserialize_json(
                data["KMSServerSideEncryption"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.devopsguru#ServiceIntegrationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.kms_server_side_encryption_integration
    import capo_devops_guru.types.logs_anomaly_detection_integration
    import capo_devops_guru.types.ops_center_integration


class ServiceIntegrationConfig(TypedDict, closed=True):
    ops_center: NotRequired[
        "capo_devops_guru.types.ops_center_integration.OpsCenterIntegration"
    ]
    """<p> Information about whether DevOps Guru is configured to create an OpsItem in Amazon Web Services Systems Manager OpsCenter for each created insight. </p>"""
    logs_anomaly_detection: NotRequired[
        "capo_devops_guru.types.logs_anomaly_detection_integration.LogsAnomalyDetectionIntegration"
    ]
    """<p> Information about whether DevOps Guru is configured to perform log anomaly detection on Amazon CloudWatch log groups. </p>"""
    kms_server_side_encryption: NotRequired[
        "capo_devops_guru.types.kms_server_side_encryption_integration.KMSServerSideEncryptionIntegration"
    ]
    """<p> Information about whether DevOps Guru is configured to encrypt server-side data using KMS. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceIntegrationConfig) -> dict:
    out: dict = {}
    if "ops_center" in value:
        import capo_devops_guru.types.ops_center_integration

        out["OpsCenter"] = capo_devops_guru.types.ops_center_integration.serialize_json(
            value["ops_center"]
        )
    if "logs_anomaly_detection" in value:
        import capo_devops_guru.types.logs_anomaly_detection_integration

        out["LogsAnomalyDetection"] = (
            capo_devops_guru.types.logs_anomaly_detection_integration.serialize_json(
                value["logs_anomaly_detection"]
            )
        )
    if "kms_server_side_encryption" in value:
        import capo_devops_guru.types.kms_server_side_encryption_integration

        out["KMSServerSideEncryption"] = (
            capo_devops_guru.types.kms_server_side_encryption_integration.serialize_json(
                value["kms_server_side_encryption"]
            )
        )
    return out


def deserialize_json(data: dict) -> ServiceIntegrationConfig:
    out: ServiceIntegrationConfig = {}  # type: ignore[typeddict-item]
    if "OpsCenter" in data:
        import capo_devops_guru.types.ops_center_integration

        out["ops_center"] = (
            capo_devops_guru.types.ops_center_integration.deserialize_json(
                data["OpsCenter"]
            )
        )
    if "LogsAnomalyDetection" in data:
        import capo_devops_guru.types.logs_anomaly_detection_integration

        out["logs_anomaly_detection"] = (
            capo_devops_guru.types.logs_anomaly_detection_integration.deserialize_json(
                data["LogsAnomalyDetection"]
            )
        )
    if "KMSServerSideEncryption" in data:
        import capo_devops_guru.types.kms_server_side_encryption_integration

        out["kms_server_side_encryption"] = (
            capo_devops_guru.types.kms_server_side_encryption_integration.deserialize_json(
                data["KMSServerSideEncryption"]
            )
        )
    return out

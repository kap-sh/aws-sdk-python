"""Generated from Smithy shape ``com.amazonaws.datazone#SparkEmrPropertiesInput``."""

from typing import TypedDict
from typing_extensions import NotRequired


class SparkEmrPropertiesInput(TypedDict):
    compute_arn: NotRequired["str"]
    """<p>The compute ARN of Spark EMR.</p>"""
    instance_profile_arn: NotRequired["str"]
    """<p>The instance profile ARN of Spark EMR.</p>"""
    java_virtual_env: NotRequired["str"]
    """<p>The java virtual env of the Spark EMR.</p>"""
    log_uri: NotRequired["str"]
    """<p>The log URI of the Spark EMR.</p>"""
    python_virtual_env: NotRequired["str"]
    """<p>The Python virtual env of the Spark EMR.</p>"""
    runtime_role: NotRequired["str"]
    """<p>The runtime role of the Spark EMR.</p>"""
    trusted_certificates_s3_uri: NotRequired["str"]
    """<p>The certificates S3 URI of the Spark EMR.</p>"""
    managed_endpoint_arn: NotRequired["str"]
    """<p>The managed endpoint ARN of the EMR on EKS cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SparkEmrPropertiesInput) -> dict:
    out: dict = {}
    if "compute_arn" in value:
        out["computeArn"] = value["compute_arn"]
    if "instance_profile_arn" in value:
        out["instanceProfileArn"] = value["instance_profile_arn"]
    if "java_virtual_env" in value:
        out["javaVirtualEnv"] = value["java_virtual_env"]
    if "log_uri" in value:
        out["logUri"] = value["log_uri"]
    if "python_virtual_env" in value:
        out["pythonVirtualEnv"] = value["python_virtual_env"]
    if "runtime_role" in value:
        out["runtimeRole"] = value["runtime_role"]
    if "trusted_certificates_s3_uri" in value:
        out["trustedCertificatesS3Uri"] = value["trusted_certificates_s3_uri"]
    if "managed_endpoint_arn" in value:
        out["managedEndpointArn"] = value["managed_endpoint_arn"]
    return out


def deserialize_json(data: dict) -> SparkEmrPropertiesInput:
    out: SparkEmrPropertiesInput = {}  # type: ignore[typeddict-item]
    if "computeArn" in data:
        out["compute_arn"] = data["computeArn"]
    if "instanceProfileArn" in data:
        out["instance_profile_arn"] = data["instanceProfileArn"]
    if "javaVirtualEnv" in data:
        out["java_virtual_env"] = data["javaVirtualEnv"]
    if "logUri" in data:
        out["log_uri"] = data["logUri"]
    if "pythonVirtualEnv" in data:
        out["python_virtual_env"] = data["pythonVirtualEnv"]
    if "runtimeRole" in data:
        out["runtime_role"] = data["runtimeRole"]
    if "trustedCertificatesS3Uri" in data:
        out["trusted_certificates_s3_uri"] = data["trustedCertificatesS3Uri"]
    if "managedEndpointArn" in data:
        out["managed_endpoint_arn"] = data["managedEndpointArn"]
    return out

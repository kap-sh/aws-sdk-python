"""Generated from Smithy shape ``com.amazonaws.datazone#SparkEmrPropertiesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_datazone.types.governance_type
    import aws_sdk_datazone.types.managed_endpoint_credentials
    import aws_sdk_datazone.types.username_password


class SparkEmrPropertiesOutput(TypedDict):
    compute_arn: NotRequired["str"]
    """<p>The compute ARN of the Spark EMR.</p>"""
    credentials: NotRequired[
        "aws_sdk_datazone.types.username_password.UsernamePassword"
    ]
    """<p>The credentials of the Spark EMR.</p>"""
    credentials_expiration: NotRequired["datetime.datetime"]
    """<p>The credential expiration of the Spark EMR.</p>"""
    governance_type: NotRequired[
        "aws_sdk_datazone.types.governance_type.GovernanceType"
    ]
    """<p>The governance type of the Spark EMR.</p>"""
    instance_profile_arn: NotRequired["str"]
    """<p>The instance profile ARN of the Spark EMR.</p>"""
    java_virtual_env: NotRequired["str"]
    """<p>The Java virtual env of the Spark EMR.</p>"""
    livy_endpoint: NotRequired["str"]
    """<p>The livy endpoint of the Spark EMR.</p>"""
    log_uri: NotRequired["str"]
    """<p>The log URI of the Spark EMR.</p>"""
    python_virtual_env: NotRequired["str"]
    """<p>The Python virtual env of the Spark EMR.</p>"""
    runtime_role: NotRequired["str"]
    """<p>The runtime role of the Spark EMR.</p>"""
    trusted_certificates_s3_uri: NotRequired["str"]
    """<p>The trusted certificate S3 URL of the Spark EMR.</p>"""
    certificate_data: NotRequired["str"]
    """<p>The certificate data of the EMR on EKS cluster.</p>"""
    managed_endpoint_arn: NotRequired["str"]
    """<p>The managed endpoint ARN of the EMR on EKS cluster.</p>"""
    managed_endpoint_credentials: NotRequired[
        "aws_sdk_datazone.types.managed_endpoint_credentials.ManagedEndpointCredentials"
    ]
    """<p>The managed endpoint credentials of the EMR on EKS cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SparkEmrPropertiesOutput) -> dict:
    out: dict = {}
    if "compute_arn" in value:
        out["computeArn"] = value["compute_arn"]
    if "credentials" in value:
        import aws_sdk_datazone.types.username_password

        out["credentials"] = aws_sdk_datazone.types.username_password.serialize_json(
            value["credentials"]
        )
    if "credentials_expiration" in value:
        import aws_sdk_datazone.types._prelude.timestamp

        out["credentialsExpiration"] = (
            aws_sdk_datazone.types._prelude.timestamp.serialize_json(
                value["credentials_expiration"]
            )
        )
    if "governance_type" in value:
        import aws_sdk_datazone.types.governance_type

        out["governanceType"] = aws_sdk_datazone.types.governance_type.serialize_json(
            value["governance_type"]
        )
    if "instance_profile_arn" in value:
        out["instanceProfileArn"] = value["instance_profile_arn"]
    if "java_virtual_env" in value:
        out["javaVirtualEnv"] = value["java_virtual_env"]
    if "livy_endpoint" in value:
        out["livyEndpoint"] = value["livy_endpoint"]
    if "log_uri" in value:
        out["logUri"] = value["log_uri"]
    if "python_virtual_env" in value:
        out["pythonVirtualEnv"] = value["python_virtual_env"]
    if "runtime_role" in value:
        out["runtimeRole"] = value["runtime_role"]
    if "trusted_certificates_s3_uri" in value:
        out["trustedCertificatesS3Uri"] = value["trusted_certificates_s3_uri"]
    if "certificate_data" in value:
        out["certificateData"] = value["certificate_data"]
    if "managed_endpoint_arn" in value:
        out["managedEndpointArn"] = value["managed_endpoint_arn"]
    if "managed_endpoint_credentials" in value:
        import aws_sdk_datazone.types.managed_endpoint_credentials

        out["managedEndpointCredentials"] = (
            aws_sdk_datazone.types.managed_endpoint_credentials.serialize_json(
                value["managed_endpoint_credentials"]
            )
        )
    return out


def deserialize_json(data: dict) -> SparkEmrPropertiesOutput:
    out: SparkEmrPropertiesOutput = {}  # type: ignore[typeddict-item]
    if "computeArn" in data:
        out["compute_arn"] = data["computeArn"]
    if "credentials" in data:
        import aws_sdk_datazone.types.username_password

        out["credentials"] = aws_sdk_datazone.types.username_password.deserialize_json(
            data["credentials"]
        )
    if "credentialsExpiration" in data:
        import aws_sdk_datazone.types._prelude.timestamp

        out["credentials_expiration"] = (
            aws_sdk_datazone.types._prelude.timestamp.deserialize_json(
                data["credentialsExpiration"]
            )
        )
    if "governanceType" in data:
        import aws_sdk_datazone.types.governance_type

        out["governance_type"] = (
            aws_sdk_datazone.types.governance_type.deserialize_json(
                data["governanceType"]
            )
        )
    if "instanceProfileArn" in data:
        out["instance_profile_arn"] = data["instanceProfileArn"]
    if "javaVirtualEnv" in data:
        out["java_virtual_env"] = data["javaVirtualEnv"]
    if "livyEndpoint" in data:
        out["livy_endpoint"] = data["livyEndpoint"]
    if "logUri" in data:
        out["log_uri"] = data["logUri"]
    if "pythonVirtualEnv" in data:
        out["python_virtual_env"] = data["pythonVirtualEnv"]
    if "runtimeRole" in data:
        out["runtime_role"] = data["runtimeRole"]
    if "trustedCertificatesS3Uri" in data:
        out["trusted_certificates_s3_uri"] = data["trustedCertificatesS3Uri"]
    if "certificateData" in data:
        out["certificate_data"] = data["certificateData"]
    if "managedEndpointArn" in data:
        out["managed_endpoint_arn"] = data["managedEndpointArn"]
    if "managedEndpointCredentials" in data:
        import aws_sdk_datazone.types.managed_endpoint_credentials

        out["managed_endpoint_credentials"] = (
            aws_sdk_datazone.types.managed_endpoint_credentials.deserialize_json(
                data["managedEndpointCredentials"]
            )
        )
    return out

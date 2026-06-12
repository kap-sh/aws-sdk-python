"""Generated from Smithy shape ``com.amazonaws.bedrock#SageMakerEndpoint``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.instance_count
    import aws_sdk_bedrock.types.instance_type
    import aws_sdk_bedrock.types.kms_key_id
    import aws_sdk_bedrock.types.role_arn
    import aws_sdk_bedrock.types.vpc_config


class SageMakerEndpoint(TypedDict):
    initial_instance_count: "aws_sdk_bedrock.types.instance_count.InstanceCount"
    """<p>The number of Amazon EC2 compute instances to deploy for initial endpoint creation.</p>"""
    instance_type: "aws_sdk_bedrock.types.instance_type.InstanceType"
    """<p>The Amazon EC2 compute instance type to deploy for hosting the model.</p>"""
    execution_role: "aws_sdk_bedrock.types.role_arn.RoleArn"
    """<p>The ARN of the IAM role that Amazon SageMaker can assume to access model artifacts and docker image for deployment on Amazon EC2 compute instances or for batch transform jobs.</p>"""
    kms_encryption_key: NotRequired["aws_sdk_bedrock.types.kms_key_id.KmsKeyId"]
    """<p>The Amazon Web Services KMS key that Amazon SageMaker uses to encrypt data on the storage volume attached to the Amazon EC2 compute instance that hosts the endpoint.</p>"""
    vpc: NotRequired["aws_sdk_bedrock.types.vpc_config.VpcConfig"]
    """<p>The VPC configuration for the endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SageMakerEndpoint) -> dict:
    out: dict = {}
    out["initialInstanceCount"] = value["initial_instance_count"]
    out["instanceType"] = value["instance_type"]
    out["executionRole"] = value["execution_role"]
    if "kms_encryption_key" in value:
        out["kmsEncryptionKey"] = value["kms_encryption_key"]
    if "vpc" in value:
        import aws_sdk_bedrock.types.vpc_config

        out["vpc"] = aws_sdk_bedrock.types.vpc_config.serialize_json(value["vpc"])
    return out


def deserialize_json(data: dict) -> SageMakerEndpoint:
    out: SageMakerEndpoint = {}  # type: ignore[typeddict-item]
    if "initialInstanceCount" in data:
        out["initial_instance_count"] = data["initialInstanceCount"]
    else:
        raise DeserializationError("SageMakerEndpoint.initial_instance_count required")
    if "instanceType" in data:
        out["instance_type"] = data["instanceType"]
    else:
        raise DeserializationError("SageMakerEndpoint.instance_type required")
    if "executionRole" in data:
        out["execution_role"] = data["executionRole"]
    else:
        raise DeserializationError("SageMakerEndpoint.execution_role required")
    if "kmsEncryptionKey" in data:
        out["kms_encryption_key"] = data["kmsEncryptionKey"]
    if "vpc" in data:
        import aws_sdk_bedrock.types.vpc_config

        out["vpc"] = aws_sdk_bedrock.types.vpc_config.deserialize_json(data["vpc"])
    return out

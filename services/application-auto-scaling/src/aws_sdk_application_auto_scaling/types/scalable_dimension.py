"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#ScalableDimension``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_auto_scaling.errors import DeserializationError

ScalableDimension: TypeAlias = Literal[
    "ecs:service:DesiredCount",
    "ec2:spot-fleet-request:TargetCapacity",
    "elasticmapreduce:instancegroup:InstanceCount",
    "appstream:fleet:DesiredCapacity",
    "dynamodb:table:ReadCapacityUnits",
    "dynamodb:table:WriteCapacityUnits",
    "dynamodb:index:ReadCapacityUnits",
    "dynamodb:index:WriteCapacityUnits",
    "rds:cluster:ReadReplicaCount",
    "sagemaker:variant:DesiredInstanceCount",
    "custom-resource:ResourceType:Property",
    "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
    "comprehend:entity-recognizer-endpoint:DesiredInferenceUnits",
    "lambda:function:ProvisionedConcurrency",
    "cassandra:table:ReadCapacityUnits",
    "cassandra:table:WriteCapacityUnits",
    "kafka:broker-storage:VolumeSize",
    "elasticache:cache-cluster:Nodes",
    "elasticache:replication-group:NodeGroups",
    "elasticache:replication-group:Replicas",
    "neptune:cluster:ReadReplicaCount",
    "sagemaker:variant:DesiredProvisionedConcurrency",
    "sagemaker:inference-component:DesiredCopyCount",
    "workspaces:workspacespool:DesiredUserSessions",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ecs:service:DesiredCount",
        "ec2:spot-fleet-request:TargetCapacity",
        "elasticmapreduce:instancegroup:InstanceCount",
        "appstream:fleet:DesiredCapacity",
        "dynamodb:table:ReadCapacityUnits",
        "dynamodb:table:WriteCapacityUnits",
        "dynamodb:index:ReadCapacityUnits",
        "dynamodb:index:WriteCapacityUnits",
        "rds:cluster:ReadReplicaCount",
        "sagemaker:variant:DesiredInstanceCount",
        "custom-resource:ResourceType:Property",
        "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
        "comprehend:entity-recognizer-endpoint:DesiredInferenceUnits",
        "lambda:function:ProvisionedConcurrency",
        "cassandra:table:ReadCapacityUnits",
        "cassandra:table:WriteCapacityUnits",
        "kafka:broker-storage:VolumeSize",
        "elasticache:cache-cluster:Nodes",
        "elasticache:replication-group:NodeGroups",
        "elasticache:replication-group:Replicas",
        "neptune:cluster:ReadReplicaCount",
        "sagemaker:variant:DesiredProvisionedConcurrency",
        "sagemaker:inference-component:DesiredCopyCount",
        "workspaces:workspacespool:DesiredUserSessions",
    )
)


def serialize_aws_json_1_1(value: ScalableDimension) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScalableDimension:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScalableDimension value: {data!r}")
    return cast(ScalableDimension, data)

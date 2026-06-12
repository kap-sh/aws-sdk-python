"""Generated from Smithy shape ``com.amazonaws.devopsguru#ServiceName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_guru.errors import DeserializationError

ServiceName: TypeAlias = Literal[
    "API_GATEWAY",
    "APPLICATION_ELB",
    "AUTO_SCALING_GROUP",
    "CLOUD_FRONT",
    "DYNAMO_DB",
    "EC2",
    "ECS",
    "EKS",
    "ELASTIC_BEANSTALK",
    "ELASTI_CACHE",
    "ELB",
    "ES",
    "KINESIS",
    "LAMBDA",
    "NAT_GATEWAY",
    "NETWORK_ELB",
    "RDS",
    "REDSHIFT",
    "ROUTE_53",
    "S3",
    "SAGE_MAKER",
    "SNS",
    "SQS",
    "STEP_FUNCTIONS",
    "SWF",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "API_GATEWAY",
        "APPLICATION_ELB",
        "AUTO_SCALING_GROUP",
        "CLOUD_FRONT",
        "DYNAMO_DB",
        "EC2",
        "ECS",
        "EKS",
        "ELASTIC_BEANSTALK",
        "ELASTI_CACHE",
        "ELB",
        "ES",
        "KINESIS",
        "LAMBDA",
        "NAT_GATEWAY",
        "NETWORK_ELB",
        "RDS",
        "REDSHIFT",
        "ROUTE_53",
        "S3",
        "SAGE_MAKER",
        "SNS",
        "SQS",
        "STEP_FUNCTIONS",
        "SWF",
    )
)


def serialize_json(value: ServiceName) -> str:
    return value


def deserialize_json(data: str) -> ServiceName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ServiceName value: {data!r}")
    return cast(ServiceName, data)

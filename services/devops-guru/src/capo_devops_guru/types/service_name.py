"""Generated from Smithy shape ``com.amazonaws.devopsguru#ServiceName``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: ServiceName) -> str:
    return value


def deserialize_json(data: str) -> ServiceName:
    return cast(ServiceName, data)

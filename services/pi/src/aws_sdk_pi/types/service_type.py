"""Generated from Smithy shape ``com.amazonaws.pi#ServiceType``."""

from typing import Literal, TypeAlias, cast

ServiceType: TypeAlias = Literal[
    "RDS",
    "DOCDB",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceType:
    return cast(ServiceType, data)

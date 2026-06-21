"""Generated from Smithy shape ``com.amazonaws.transfer#ConnectorEgressType``."""

from typing import Literal, TypeAlias, cast

ConnectorEgressType: TypeAlias = Literal[
    "SERVICE_MANAGED",
    "VPC_LATTICE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectorEgressType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConnectorEgressType:
    return cast(ConnectorEgressType, data)

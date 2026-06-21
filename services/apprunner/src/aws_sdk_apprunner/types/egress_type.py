"""Generated from Smithy shape ``com.amazonaws.apprunner#EgressType``."""

from typing import Literal, TypeAlias, cast

EgressType: TypeAlias = Literal[
    "DEFAULT",
    "VPC",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EgressType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EgressType:
    return cast(EgressType, data)

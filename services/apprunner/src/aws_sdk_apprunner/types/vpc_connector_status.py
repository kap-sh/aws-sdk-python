"""Generated from Smithy shape ``com.amazonaws.apprunner#VpcConnectorStatus``."""

from typing import Literal, TypeAlias, cast

VpcConnectorStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VpcConnectorStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> VpcConnectorStatus:
    return cast(VpcConnectorStatus, data)

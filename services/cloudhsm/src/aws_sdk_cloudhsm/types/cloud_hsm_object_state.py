"""Generated from Smithy shape ``com.amazonaws.cloudhsm#CloudHsmObjectState``."""

from typing import Literal, TypeAlias, cast

CloudHsmObjectState: TypeAlias = Literal[
    "READY",
    "UPDATING",
    "DEGRADED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudHsmObjectState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CloudHsmObjectState:
    return cast(CloudHsmObjectState, data)

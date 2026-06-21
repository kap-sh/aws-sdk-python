"""Generated from Smithy shape ``com.amazonaws.cloudhsm#HsmStatus``."""

from typing import Literal, TypeAlias, cast

HsmStatus: TypeAlias = Literal[
    "PENDING",
    "RUNNING",
    "UPDATING",
    "SUSPENDED",
    "TERMINATING",
    "TERMINATED",
    "DEGRADED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HsmStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HsmStatus:
    return cast(HsmStatus, data)

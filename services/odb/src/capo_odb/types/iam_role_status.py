"""Generated from Smithy shape ``com.amazonaws.odb#IamRoleStatus``."""

from typing import Literal, TypeAlias, cast

IamRoleStatus: TypeAlias = Literal[
    "ASSOCIATING",
    "DISASSOCIATING",
    "FAILED",
    "CONNECTED",
    "DISCONNECTED",
    "PARTIALLY_CONNECTED",
    "UNKNOWN",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IamRoleStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IamRoleStatus:
    return cast(IamRoleStatus, data)

"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#AliasState``."""

from typing import Literal, TypeAlias, cast

AliasState: TypeAlias = Literal[
    "Active",
    "PendingDeletion",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AliasState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AliasState:
    return cast(AliasState, data)

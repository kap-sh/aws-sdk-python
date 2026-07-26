"""Generated from Smithy shape ``com.amazonaws.dynamodb#GlobalTableStatus``."""

from typing import Literal, TypeAlias, cast

GlobalTableStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "DELETING",
    "UPDATING",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GlobalTableStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> GlobalTableStatus:
    return cast(GlobalTableStatus, data)

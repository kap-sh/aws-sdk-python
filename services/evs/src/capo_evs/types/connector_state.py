"""Generated from Smithy shape ``com.amazonaws.evs#ConnectorState``."""

from typing import Literal, TypeAlias, cast

ConnectorState: TypeAlias = Literal[
    "CREATING",
    "CREATE_FAILED",
    "ACTIVE",
    "UPDATING",
    "UPDATE_FAILED",
    "DELETING",
    "DELETED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConnectorState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ConnectorState:
    return cast(ConnectorState, data)

"""Generated from Smithy shape ``com.amazonaws.glue#TriggerState``."""

from typing import Literal, TypeAlias, cast

TriggerState: TypeAlias = Literal[
    "CREATING",
    "CREATED",
    "ACTIVATING",
    "ACTIVATED",
    "DEACTIVATING",
    "DEACTIVATED",
    "DELETING",
    "UPDATING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TriggerState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TriggerState:
    return cast(TriggerState, data)

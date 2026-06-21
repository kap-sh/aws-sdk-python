"""Generated from Smithy shape ``com.amazonaws.codestarconnections#TriggerResourceUpdateOn``."""

from typing import Literal, TypeAlias, cast

TriggerResourceUpdateOn: TypeAlias = Literal[
    "ANY_CHANGE",
    "FILE_CHANGE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TriggerResourceUpdateOn) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TriggerResourceUpdateOn:
    return cast(TriggerResourceUpdateOn, data)

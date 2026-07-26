"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ModelPromoteMode``."""

from typing import Literal, TypeAlias, cast

ModelPromoteMode: TypeAlias = Literal[
    "MANAGED",
    "MANUAL",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ModelPromoteMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ModelPromoteMode:
    return cast(ModelPromoteMode, data)

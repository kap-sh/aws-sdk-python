"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#UpdateMode``."""

from typing import Literal, TypeAlias, cast

UpdateMode: TypeAlias = Literal[
    "Overwrite",
    "Merge",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> UpdateMode:
    return cast(UpdateMode, data)

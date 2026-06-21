"""Generated from Smithy shape ``com.amazonaws.glue#ResourceAction``."""

from typing import Literal, TypeAlias, cast

ResourceAction: TypeAlias = Literal[
    "UPDATE",
    "CREATE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceAction:
    return cast(ResourceAction, data)

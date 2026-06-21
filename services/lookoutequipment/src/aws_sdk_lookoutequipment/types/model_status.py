"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ModelStatus``."""

from typing import Literal, TypeAlias, cast

ModelStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCESS",
    "FAILED",
    "IMPORT_IN_PROGRESS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ModelStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ModelStatus:
    return cast(ModelStatus, data)

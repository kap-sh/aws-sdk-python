"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ModelVersionStatus``."""

from typing import Literal, TypeAlias, cast

ModelVersionStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCESS",
    "FAILED",
    "IMPORT_IN_PROGRESS",
    "CANCELED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ModelVersionStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ModelVersionStatus:
    return cast(ModelVersionStatus, data)

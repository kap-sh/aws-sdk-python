"""Generated from Smithy shape ``com.amazonaws.odb#ComputeModel``."""

from typing import Literal, TypeAlias, cast

ComputeModel: TypeAlias = Literal[
    "ECPU",
    "OCPU",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ComputeModel) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ComputeModel:
    return cast(ComputeModel, data)

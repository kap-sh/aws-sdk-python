"""Generated from Smithy shape ``com.amazonaws.batch#ComputeEnvironmentDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.compute_environment_detail

ComputeEnvironmentDetailList: TypeAlias = list[
    "aws_sdk_batch.types.compute_environment_detail.ComputeEnvironmentDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: ComputeEnvironmentDetailList) -> list:
    import aws_sdk_batch.types.compute_environment_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_batch.types.compute_environment_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> ComputeEnvironmentDetailList:
    import aws_sdk_batch.types.compute_environment_detail

    out: ComputeEnvironmentDetailList = []
    for item in data:
        out.append(
            aws_sdk_batch.types.compute_environment_detail.deserialize_json(item)
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.mturk#WorkerBlockList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mturk.types.worker_block

WorkerBlockList: TypeAlias = list["aws_sdk_mturk.types.worker_block.WorkerBlock"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkerBlockList) -> list:
    import aws_sdk_mturk.types.worker_block

    out: list = []
    for item in value:
        out.append(aws_sdk_mturk.types.worker_block.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> WorkerBlockList:
    import aws_sdk_mturk.types.worker_block

    out: WorkerBlockList = []
    for item in data:
        out.append(aws_sdk_mturk.types.worker_block.deserialize_aws_json_1_1(item))
    return out

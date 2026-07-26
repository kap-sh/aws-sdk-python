"""Generated from Smithy shape ``com.amazonaws.mturk#WorkerBlockList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mturk.types.worker_block

WorkerBlockList: TypeAlias = list["capo_mturk.types.worker_block.WorkerBlock"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkerBlockList) -> list:
    import capo_mturk.types.worker_block

    out: list = []
    for item in value:
        out.append(capo_mturk.types.worker_block.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> WorkerBlockList:
    import capo_mturk.types.worker_block

    out: WorkerBlockList = []
    for item in data:
        out.append(capo_mturk.types.worker_block.deserialize_aws_json_1_1(item))
    return out

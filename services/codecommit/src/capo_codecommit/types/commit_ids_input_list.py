"""Generated from Smithy shape ``com.amazonaws.codecommit#CommitIdsInputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecommit.types.object_id

CommitIdsInputList: TypeAlias = list["capo_codecommit.types.object_id.ObjectId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CommitIdsInputList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> CommitIdsInputList:
    return list(data)

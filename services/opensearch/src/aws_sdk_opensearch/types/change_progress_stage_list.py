"""Generated from Smithy shape ``com.amazonaws.opensearch#ChangeProgressStageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.change_progress_stage

ChangeProgressStageList: TypeAlias = list[
    "aws_sdk_opensearch.types.change_progress_stage.ChangeProgressStage"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChangeProgressStageList) -> list:
    import aws_sdk_opensearch.types.change_progress_stage

    out: list = []
    for item in value:
        out.append(aws_sdk_opensearch.types.change_progress_stage.serialize_json(item))
    return out


def deserialize_json(data: list) -> ChangeProgressStageList:
    import aws_sdk_opensearch.types.change_progress_stage

    out: ChangeProgressStageList = []
    for item in data:
        out.append(
            aws_sdk_opensearch.types.change_progress_stage.deserialize_json(item)
        )
    return out

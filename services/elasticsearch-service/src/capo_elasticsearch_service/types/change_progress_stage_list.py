"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ChangeProgressStageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.change_progress_stage

ChangeProgressStageList: TypeAlias = list[
    "capo_elasticsearch_service.types.change_progress_stage.ChangeProgressStage"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChangeProgressStageList) -> list:
    import capo_elasticsearch_service.types.change_progress_stage

    out: list = []
    for item in value:
        out.append(
            capo_elasticsearch_service.types.change_progress_stage.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ChangeProgressStageList:
    import capo_elasticsearch_service.types.change_progress_stage

    out: ChangeProgressStageList = []
    for item in data:
        out.append(
            capo_elasticsearch_service.types.change_progress_stage.deserialize_json(
                item
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#PipelineInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.pipeline_info

PipelineInfoList: TypeAlias = list[
    "capo_migrationhubstrategy.types.pipeline_info.PipelineInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: PipelineInfoList) -> list:
    import capo_migrationhubstrategy.types.pipeline_info

    out: list = []
    for item in value:
        out.append(capo_migrationhubstrategy.types.pipeline_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> PipelineInfoList:
    import capo_migrationhubstrategy.types.pipeline_info

    out: PipelineInfoList = []
    for item in data:
        out.append(capo_migrationhubstrategy.types.pipeline_info.deserialize_json(item))
    return out

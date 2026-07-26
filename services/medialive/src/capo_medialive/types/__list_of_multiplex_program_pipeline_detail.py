"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfMultiplexProgramPipelineDetail``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.multiplex_program_pipeline_detail

__listOfMultiplexProgramPipelineDetail: TypeAlias = list[
    "capo_medialive.types.multiplex_program_pipeline_detail.MultiplexProgramPipelineDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfMultiplexProgramPipelineDetail) -> list:
    import capo_medialive.types.multiplex_program_pipeline_detail

    out: list = []
    for item in value:
        out.append(
            capo_medialive.types.multiplex_program_pipeline_detail.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfMultiplexProgramPipelineDetail:
    import capo_medialive.types.multiplex_program_pipeline_detail

    out: __listOfMultiplexProgramPipelineDetail = []
    for item in data:
        out.append(
            capo_medialive.types.multiplex_program_pipeline_detail.deserialize_json(
                item
            )
        )
    return out

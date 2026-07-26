"""Generated from Smithy shape ``com.amazonaws.osis#PipelineDestinationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_osis.types.pipeline_destination

PipelineDestinationList: TypeAlias = list[
    "capo_osis.types.pipeline_destination.PipelineDestination"
]


# --- restJson1 ser/de ---
def serialize_json(value: PipelineDestinationList) -> list:
    import capo_osis.types.pipeline_destination

    out: list = []
    for item in value:
        out.append(capo_osis.types.pipeline_destination.serialize_json(item))
    return out


def deserialize_json(data: list) -> PipelineDestinationList:
    import capo_osis.types.pipeline_destination

    out: PipelineDestinationList = []
    for item in data:
        out.append(capo_osis.types.pipeline_destination.deserialize_json(item))
    return out

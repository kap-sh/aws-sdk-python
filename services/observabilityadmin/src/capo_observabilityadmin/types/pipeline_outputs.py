"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#PipelineOutputs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_observabilityadmin.types.pipeline_output

PipelineOutputs: TypeAlias = list[
    "capo_observabilityadmin.types.pipeline_output.PipelineOutput"
]


# --- restJson1 ser/de ---
def serialize_json(value: PipelineOutputs) -> list:
    import capo_observabilityadmin.types.pipeline_output

    out: list = []
    for item in value:
        out.append(capo_observabilityadmin.types.pipeline_output.serialize_json(item))
    return out


def deserialize_json(data: list) -> PipelineOutputs:
    import capo_observabilityadmin.types.pipeline_output

    out: PipelineOutputs = []
    for item in data:
        out.append(capo_observabilityadmin.types.pipeline_output.deserialize_json(item))
    return out

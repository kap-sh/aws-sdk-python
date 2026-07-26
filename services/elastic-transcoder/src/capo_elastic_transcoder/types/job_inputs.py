"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#JobInputs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elastic_transcoder.types.job_input

JobInputs: TypeAlias = list["capo_elastic_transcoder.types.job_input.JobInput"]


# --- restJson1 ser/de ---
def serialize_json(value: JobInputs) -> list:
    import capo_elastic_transcoder.types.job_input

    out: list = []
    for item in value:
        out.append(capo_elastic_transcoder.types.job_input.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobInputs:
    import capo_elastic_transcoder.types.job_input

    out: JobInputs = []
    for item in data:
        out.append(capo_elastic_transcoder.types.job_input.deserialize_json(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.deadline#JobParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.job_parameter
    import capo_deadline.types.string

JobParameters: TypeAlias = dict[
    "capo_deadline.types.string.String",
    "capo_deadline.types.job_parameter.JobParameter",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: JobParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_deadline.types.job_parameter

        out[key] = capo_deadline.types.job_parameter.serialize_json(value)
    return out


def deserialize_json(data: dict) -> JobParameters:
    out: JobParameters = {}
    for key, value in data.items():
        import capo_deadline.types.job_parameter

        out[key] = capo_deadline.types.job_parameter.deserialize_json(value)
    return out

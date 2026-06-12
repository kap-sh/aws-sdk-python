"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#CreateJobOutputs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.create_job_output

CreateJobOutputs: TypeAlias = list[
    "aws_sdk_elastic_transcoder.types.create_job_output.CreateJobOutput"
]


# --- restJson1 ser/de ---
def serialize_json(value: CreateJobOutputs) -> list:
    import aws_sdk_elastic_transcoder.types.create_job_output

    out: list = []
    for item in value:
        out.append(
            aws_sdk_elastic_transcoder.types.create_job_output.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CreateJobOutputs:
    import aws_sdk_elastic_transcoder.types.create_job_output

    out: CreateJobOutputs = []
    for item in data:
        out.append(
            aws_sdk_elastic_transcoder.types.create_job_output.deserialize_json(item)
        )
    return out

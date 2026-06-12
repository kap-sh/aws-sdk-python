"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#JobOutputs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.job_output

JobOutputs: TypeAlias = list["aws_sdk_elastic_transcoder.types.job_output.JobOutput"]


# --- restJson1 ser/de ---
def serialize_json(value: JobOutputs) -> list:
    import aws_sdk_elastic_transcoder.types.job_output

    out: list = []
    for item in value:
        out.append(aws_sdk_elastic_transcoder.types.job_output.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobOutputs:
    import aws_sdk_elastic_transcoder.types.job_output

    out: JobOutputs = []
    for item in data:
        out.append(aws_sdk_elastic_transcoder.types.job_output.deserialize_json(item))
    return out

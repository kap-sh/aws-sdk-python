"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#Jobs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.job

Jobs: TypeAlias = list["aws_sdk_elastic_transcoder.types.job.Job"]


# --- restJson1 ser/de ---
def serialize_json(value: Jobs) -> list:
    import aws_sdk_elastic_transcoder.types.job

    out: list = []
    for item in value:
        out.append(aws_sdk_elastic_transcoder.types.job.serialize_json(item))
    return out


def deserialize_json(data: list) -> Jobs:
    import aws_sdk_elastic_transcoder.types.job

    out: Jobs = []
    for item in data:
        out.append(aws_sdk_elastic_transcoder.types.job.deserialize_json(item))
    return out

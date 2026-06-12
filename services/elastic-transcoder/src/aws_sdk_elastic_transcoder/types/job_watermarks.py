"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#JobWatermarks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.job_watermark

JobWatermarks: TypeAlias = list[
    "aws_sdk_elastic_transcoder.types.job_watermark.JobWatermark"
]


# --- restJson1 ser/de ---
def serialize_json(value: JobWatermarks) -> list:
    import aws_sdk_elastic_transcoder.types.job_watermark

    out: list = []
    for item in value:
        out.append(aws_sdk_elastic_transcoder.types.job_watermark.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobWatermarks:
    import aws_sdk_elastic_transcoder.types.job_watermark

    out: JobWatermarks = []
    for item in data:
        out.append(
            aws_sdk_elastic_transcoder.types.job_watermark.deserialize_json(item)
        )
    return out

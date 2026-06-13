"""Generated from Smithy shape ``com.amazonaws.entityresolution#JobOutputSourceConfig``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.job_output_source

JobOutputSourceConfig: TypeAlias = list[
    "aws_sdk_entityresolution.types.job_output_source.JobOutputSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: JobOutputSourceConfig) -> list:
    import aws_sdk_entityresolution.types.job_output_source

    out: list = []
    for item in value:
        out.append(
            aws_sdk_entityresolution.types.job_output_source.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> JobOutputSourceConfig:
    import aws_sdk_entityresolution.types.job_output_source

    out: JobOutputSourceConfig = []
    for item in data:
        out.append(
            aws_sdk_entityresolution.types.job_output_source.deserialize_json(item)
        )
    return out

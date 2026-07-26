"""Generated from Smithy shape ``com.amazonaws.snowball#JobMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_snowball.types.job_metadata

JobMetadataList: TypeAlias = list["capo_snowball.types.job_metadata.JobMetadata"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobMetadataList) -> list:
    import capo_snowball.types.job_metadata

    out: list = []
    for item in value:
        out.append(capo_snowball.types.job_metadata.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> JobMetadataList:
    import capo_snowball.types.job_metadata

    out: JobMetadataList = []
    for item in data:
        out.append(capo_snowball.types.job_metadata.deserialize_aws_json_1_1(item))
    return out

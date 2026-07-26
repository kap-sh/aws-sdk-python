"""Generated from Smithy shape ``com.amazonaws.transfer#S3Tags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transfer.types.s3_tag

S3Tags: TypeAlias = list["capo_transfer.types.s3_tag.S3Tag"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3Tags) -> list:
    import capo_transfer.types.s3_tag

    out: list = []
    for item in value:
        out.append(capo_transfer.types.s3_tag.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> S3Tags:
    import capo_transfer.types.s3_tag

    out: S3Tags = []
    for item in data:
        out.append(capo_transfer.types.s3_tag.deserialize_aws_json_1_1(item))
    return out

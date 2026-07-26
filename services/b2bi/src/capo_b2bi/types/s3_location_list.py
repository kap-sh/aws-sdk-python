"""Generated from Smithy shape ``com.amazonaws.b2bi#S3LocationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_b2bi.types.s3_location

S3LocationList: TypeAlias = list["capo_b2bi.types.s3_location.S3Location"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: S3LocationList) -> list:
    import capo_b2bi.types.s3_location

    out: list = []
    for item in value:
        out.append(capo_b2bi.types.s3_location.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> S3LocationList:
    import capo_b2bi.types.s3_location

    out: S3LocationList = []
    for item in data:
        out.append(capo_b2bi.types.s3_location.deserialize_aws_json_1_0(item))
    return out

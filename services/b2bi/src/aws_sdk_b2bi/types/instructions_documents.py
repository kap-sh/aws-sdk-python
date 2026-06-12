"""Generated from Smithy shape ``com.amazonaws.b2bi#InstructionsDocuments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.s3_location

InstructionsDocuments: TypeAlias = list["aws_sdk_b2bi.types.s3_location.S3Location"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InstructionsDocuments) -> list:
    import aws_sdk_b2bi.types.s3_location

    out: list = []
    for item in value:
        out.append(aws_sdk_b2bi.types.s3_location.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> InstructionsDocuments:
    import aws_sdk_b2bi.types.s3_location

    out: InstructionsDocuments = []
    for item in data:
        out.append(aws_sdk_b2bi.types.s3_location.deserialize_aws_json_1_0(item))
    return out

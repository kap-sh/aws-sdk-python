"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ListOfDiscardedFiles``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.s3_object

ListOfDiscardedFiles: TypeAlias = list[
    "aws_sdk_lookoutequipment.types.s3_object.S3Object"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListOfDiscardedFiles) -> list:
    import aws_sdk_lookoutequipment.types.s3_object

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lookoutequipment.types.s3_object.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ListOfDiscardedFiles:
    import aws_sdk_lookoutequipment.types.s3_object

    out: ListOfDiscardedFiles = []
    for item in data:
        out.append(
            aws_sdk_lookoutequipment.types.s3_object.deserialize_aws_json_1_0(item)
        )
    return out

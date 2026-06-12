"""Generated from Smithy shape ``com.amazonaws.ecr#ImageIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecr.types.image_identifier

ImageIdentifierList: TypeAlias = list[
    "aws_sdk_ecr.types.image_identifier.ImageIdentifier"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageIdentifierList) -> list:
    import aws_sdk_ecr.types.image_identifier

    out: list = []
    for item in value:
        out.append(aws_sdk_ecr.types.image_identifier.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ImageIdentifierList:
    import aws_sdk_ecr.types.image_identifier

    out: ImageIdentifierList = []
    for item in data:
        out.append(aws_sdk_ecr.types.image_identifier.deserialize_aws_json_1_1(item))
    return out

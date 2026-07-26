"""Generated from Smithy shape ``com.amazonaws.ecr#ImageIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecr.types.image_identifier

ImageIdentifierList: TypeAlias = list["capo_ecr.types.image_identifier.ImageIdentifier"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageIdentifierList) -> list:
    import capo_ecr.types.image_identifier

    out: list = []
    for item in value:
        out.append(capo_ecr.types.image_identifier.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ImageIdentifierList:
    import capo_ecr.types.image_identifier

    out: ImageIdentifierList = []
    for item in data:
        out.append(capo_ecr.types.image_identifier.deserialize_aws_json_1_1(item))
    return out

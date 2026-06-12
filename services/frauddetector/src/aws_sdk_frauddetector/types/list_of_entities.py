"""Generated from Smithy shape ``com.amazonaws.frauddetector#listOfEntities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.entity

listOfEntities: TypeAlias = list["aws_sdk_frauddetector.types.entity.Entity"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: listOfEntities) -> list:
    import aws_sdk_frauddetector.types.entity

    out: list = []
    for item in value:
        out.append(aws_sdk_frauddetector.types.entity.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> listOfEntities:
    import aws_sdk_frauddetector.types.entity

    out: listOfEntities = []
    for item in data:
        out.append(aws_sdk_frauddetector.types.entity.deserialize_aws_json_1_1(item))
    return out

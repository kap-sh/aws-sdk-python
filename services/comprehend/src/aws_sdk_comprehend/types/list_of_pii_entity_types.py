"""Generated from Smithy shape ``com.amazonaws.comprehend#ListOfPiiEntityTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.pii_entity_type

ListOfPiiEntityTypes: TypeAlias = list[
    "aws_sdk_comprehend.types.pii_entity_type.PiiEntityType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfPiiEntityTypes) -> list:
    import aws_sdk_comprehend.types.pii_entity_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_comprehend.types.pii_entity_type.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfPiiEntityTypes:
    import aws_sdk_comprehend.types.pii_entity_type

    out: ListOfPiiEntityTypes = []
    for item in data:
        out.append(
            aws_sdk_comprehend.types.pii_entity_type.deserialize_aws_json_1_1(item)
        )
    return out

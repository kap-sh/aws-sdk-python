"""Generated from Smithy shape ``com.amazonaws.comprehend#ListOfRelationships``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.relationships_list_item

ListOfRelationships: TypeAlias = list[
    "aws_sdk_comprehend.types.relationships_list_item.RelationshipsListItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfRelationships) -> list:
    import aws_sdk_comprehend.types.relationships_list_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_comprehend.types.relationships_list_item.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfRelationships:
    import aws_sdk_comprehend.types.relationships_list_item

    out: ListOfRelationships = []
    for item in data:
        out.append(
            aws_sdk_comprehend.types.relationships_list_item.deserialize_aws_json_1_1(
                item
            )
        )
    return out

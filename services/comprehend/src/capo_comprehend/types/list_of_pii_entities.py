"""Generated from Smithy shape ``com.amazonaws.comprehend#ListOfPiiEntities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehend.types.pii_entity

ListOfPiiEntities: TypeAlias = list["capo_comprehend.types.pii_entity.PiiEntity"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfPiiEntities) -> list:
    import capo_comprehend.types.pii_entity

    out: list = []
    for item in value:
        out.append(capo_comprehend.types.pii_entity.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfPiiEntities:
    import capo_comprehend.types.pii_entity

    out: ListOfPiiEntities = []
    for item in data:
        out.append(capo_comprehend.types.pii_entity.deserialize_aws_json_1_1(item))
    return out

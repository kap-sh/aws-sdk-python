"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#EntityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehendmedical.types.entity

EntityList: TypeAlias = list["capo_comprehendmedical.types.entity.Entity"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityList) -> list:
    import capo_comprehendmedical.types.entity

    out: list = []
    for item in value:
        out.append(capo_comprehendmedical.types.entity.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EntityList:
    import capo_comprehendmedical.types.entity

    out: EntityList = []
    for item in data:
        out.append(capo_comprehendmedical.types.entity.deserialize_aws_json_1_1(item))
    return out

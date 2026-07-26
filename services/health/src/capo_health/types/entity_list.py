"""Generated from Smithy shape ``com.amazonaws.health#EntityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.affected_entity

EntityList: TypeAlias = list["capo_health.types.affected_entity.AffectedEntity"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityList) -> list:
    import capo_health.types.affected_entity

    out: list = []
    for item in value:
        out.append(capo_health.types.affected_entity.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EntityList:
    import capo_health.types.affected_entity

    out: EntityList = []
    for item in data:
        out.append(capo_health.types.affected_entity.deserialize_aws_json_1_1(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.kendra#EntityIdsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.entity_id

EntityIdsList: TypeAlias = list["aws_sdk_kendra.types.entity_id.EntityId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityIdsList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> EntityIdsList:
    return list(data)

"""Generated from Smithy shape ``com.amazonaws.lightsail#RelationalDatabaseEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.relational_database_event

RelationalDatabaseEventList: TypeAlias = list[
    "capo_lightsail.types.relational_database_event.RelationalDatabaseEvent"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelationalDatabaseEventList) -> list:
    import capo_lightsail.types.relational_database_event

    out: list = []
    for item in value:
        out.append(
            capo_lightsail.types.relational_database_event.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RelationalDatabaseEventList:
    import capo_lightsail.types.relational_database_event

    out: RelationalDatabaseEventList = []
    for item in data:
        out.append(
            capo_lightsail.types.relational_database_event.deserialize_aws_json_1_1(
                item
            )
        )
    return out

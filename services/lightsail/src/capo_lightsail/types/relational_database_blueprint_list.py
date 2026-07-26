"""Generated from Smithy shape ``com.amazonaws.lightsail#RelationalDatabaseBlueprintList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.relational_database_blueprint

RelationalDatabaseBlueprintList: TypeAlias = list[
    "capo_lightsail.types.relational_database_blueprint.RelationalDatabaseBlueprint"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelationalDatabaseBlueprintList) -> list:
    import capo_lightsail.types.relational_database_blueprint

    out: list = []
    for item in value:
        out.append(
            capo_lightsail.types.relational_database_blueprint.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RelationalDatabaseBlueprintList:
    import capo_lightsail.types.relational_database_blueprint

    out: RelationalDatabaseBlueprintList = []
    for item in data:
        out.append(
            capo_lightsail.types.relational_database_blueprint.deserialize_aws_json_1_1(
                item
            )
        )
    return out

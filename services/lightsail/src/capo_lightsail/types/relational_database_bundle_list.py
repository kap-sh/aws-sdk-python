"""Generated from Smithy shape ``com.amazonaws.lightsail#RelationalDatabaseBundleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.relational_database_bundle

RelationalDatabaseBundleList: TypeAlias = list[
    "capo_lightsail.types.relational_database_bundle.RelationalDatabaseBundle"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelationalDatabaseBundleList) -> list:
    import capo_lightsail.types.relational_database_bundle

    out: list = []
    for item in value:
        out.append(
            capo_lightsail.types.relational_database_bundle.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RelationalDatabaseBundleList:
    import capo_lightsail.types.relational_database_bundle

    out: RelationalDatabaseBundleList = []
    for item in data:
        out.append(
            capo_lightsail.types.relational_database_bundle.deserialize_aws_json_1_1(
                item
            )
        )
    return out

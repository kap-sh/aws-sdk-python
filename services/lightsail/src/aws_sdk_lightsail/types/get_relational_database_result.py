"""Generated from Smithy shape ``com.amazonaws.lightsail#GetRelationalDatabaseResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.relational_database


class GetRelationalDatabaseResult(TypedDict):
    relational_database: NotRequired[
        "aws_sdk_lightsail.types.relational_database.RelationalDatabase"
    ]
    """<p>An object describing the specified database.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRelationalDatabaseResult) -> dict:
    out: dict = {}
    if "relational_database" in value:
        import aws_sdk_lightsail.types.relational_database

        out["relationalDatabase"] = (
            aws_sdk_lightsail.types.relational_database.serialize_aws_json_1_1(
                value["relational_database"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRelationalDatabaseResult:
    out: GetRelationalDatabaseResult = {}  # type: ignore[typeddict-item]
    if "relationalDatabase" in data:
        import aws_sdk_lightsail.types.relational_database

        out["relational_database"] = (
            aws_sdk_lightsail.types.relational_database.deserialize_aws_json_1_1(
                data["relationalDatabase"]
            )
        )
    return out

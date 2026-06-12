"""Generated from Smithy shape ``com.amazonaws.glue#GetDatabaseResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.database


class GetDatabaseResponse(TypedDict):
    database: NotRequired["aws_sdk_glue.types.database.Database"]
    """<p>The definition of the specified database in the Data Catalog.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDatabaseResponse) -> dict:
    out: dict = {}
    if "database" in value:
        import aws_sdk_glue.types.database

        out["Database"] = aws_sdk_glue.types.database.serialize_aws_json_1_1(
            value["database"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDatabaseResponse:
    out: GetDatabaseResponse = {}  # type: ignore[typeddict-item]
    if "Database" in data:
        import aws_sdk_glue.types.database

        out["database"] = aws_sdk_glue.types.database.deserialize_aws_json_1_1(
            data["Database"]
        )
    return out

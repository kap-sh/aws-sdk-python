"""Generated from Smithy shape ``com.amazonaws.athena#GetDatabaseOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_athena.types.database


class GetDatabaseOutput(TypedDict):
    database: NotRequired["aws_sdk_athena.types.database.Database"]
    """<p>The database returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDatabaseOutput) -> dict:
    out: dict = {}
    if "database" in value:
        import aws_sdk_athena.types.database

        out["Database"] = aws_sdk_athena.types.database.serialize_aws_json_1_1(
            value["database"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDatabaseOutput:
    out: GetDatabaseOutput = {}  # type: ignore[typeddict-item]
    if "Database" in data:
        import aws_sdk_athena.types.database

        out["database"] = aws_sdk_athena.types.database.deserialize_aws_json_1_1(
            data["Database"]
        )
    return out

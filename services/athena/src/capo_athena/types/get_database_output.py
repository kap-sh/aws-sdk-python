"""Generated from Smithy shape ``com.amazonaws.athena#GetDatabaseOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.database


class GetDatabaseOutput(TypedDict, closed=True):
    database: NotRequired["capo_athena.types.database.Database"]
    """<p>The database returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDatabaseOutput) -> dict:
    out: dict = {}
    if "database" in value:
        import capo_athena.types.database

        out["Database"] = capo_athena.types.database.serialize_aws_json_1_1(
            value["database"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDatabaseOutput:
    out: GetDatabaseOutput = {}  # type: ignore[typeddict-item]
    if "Database" in data:
        import capo_athena.types.database

        out["database"] = capo_athena.types.database.deserialize_aws_json_1_1(
            data["Database"]
        )
    return out

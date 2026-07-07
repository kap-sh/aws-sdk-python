"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#StatementProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string


class StatementProperties(TypedDict, closed=True):
    definition: "aws_sdk_database_migration_service.types.string.String"
    """<p>The SQL text of the statement.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StatementProperties) -> dict:
    out: dict = {}
    out["Definition"] = value["definition"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StatementProperties:
    out: StatementProperties = {}  # type: ignore[typeddict-item]
    if "Definition" in data:
        out["definition"] = data["Definition"]
    else:
        raise DeserializationError("StatementProperties.definition required")
    return out

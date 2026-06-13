"""Generated from Smithy shape ``com.amazonaws.datazone#RelationalFilterConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.filter_expressions


class RelationalFilterConfiguration(TypedDict):
    database_name: "str"
    """<p>The database name specified in the relational filter configuration for the data source.</p>"""
    schema_name: NotRequired["str"]
    """<p>The schema name specified in the relational filter configuration for the data source.</p>"""
    filter_expressions: NotRequired[
        "aws_sdk_datazone.types.filter_expressions.FilterExpressions"
    ]
    """<p>The filter expressions specified in the relational filter configuration for the data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RelationalFilterConfiguration) -> dict:
    out: dict = {}
    out["databaseName"] = value["database_name"]
    if "schema_name" in value:
        out["schemaName"] = value["schema_name"]
    if "filter_expressions" in value:
        import aws_sdk_datazone.types.filter_expressions

        out["filterExpressions"] = (
            aws_sdk_datazone.types.filter_expressions.serialize_json(
                value["filter_expressions"]
            )
        )
    return out


def deserialize_json(data: dict) -> RelationalFilterConfiguration:
    out: RelationalFilterConfiguration = {}  # type: ignore[typeddict-item]
    if "databaseName" in data:
        out["database_name"] = data["databaseName"]
    else:
        raise DeserializationError(
            "RelationalFilterConfiguration.database_name required"
        )
    if "schemaName" in data:
        out["schema_name"] = data["schemaName"]
    if "filterExpressions" in data:
        import aws_sdk_datazone.types.filter_expressions

        out["filter_expressions"] = (
            aws_sdk_datazone.types.filter_expressions.deserialize_json(
                data["filterExpressions"]
            )
        )
    return out

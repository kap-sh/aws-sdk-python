"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#DataQuery``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bcm_data_exports.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bcm_data_exports.types.query_statement
    import aws_sdk_bcm_data_exports.types.table_configurations

class DataQuery(TypedDict):
    query_statement: "aws_sdk_bcm_data_exports.types.query_statement.QueryStatement"
    """<p>The query statement.</p>"""
    table_configurations: NotRequired["aws_sdk_bcm_data_exports.types.table_configurations.TableConfigurations"]
    """<p>The table configuration.</p>"""

# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQuery) -> dict:
    out: dict = {}
    out["QueryStatement"] = value["query_statement"]
    if "table_configurations" in value:
        import aws_sdk_bcm_data_exports.types.table_configurations
        out["TableConfigurations"] = aws_sdk_bcm_data_exports.types.table_configurations.serialize_aws_json_1_1(value["table_configurations"])
    return out


def deserialize_aws_json_1_1(data: dict) -> DataQuery:
    out: DataQuery = {}  # type: ignore[typeddict-item]
    if "QueryStatement" in data:
        out["query_statement"] = data["QueryStatement"]
    else:
        raise DeserializationError("DataQuery.query_statement required")
    if "TableConfigurations" in data:
        import aws_sdk_bcm_data_exports.types.table_configurations
        out["table_configurations"] = aws_sdk_bcm_data_exports.types.table_configurations.deserialize_aws_json_1_1(data["TableConfigurations"])
    return out
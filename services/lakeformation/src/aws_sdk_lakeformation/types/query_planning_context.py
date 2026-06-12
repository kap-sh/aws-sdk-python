"""Generated from Smithy shape ``com.amazonaws.lakeformation#QueryPlanningContext``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.catalog_id_string
    import aws_sdk_lakeformation.types.query_parameter_map
    import aws_sdk_lakeformation.types.query_planning_context_database_name_string
    import aws_sdk_lakeformation.types.timestamp
    import aws_sdk_lakeformation.types.transaction_id_string


class QueryPlanningContext(TypedDict):
    catalog_id: NotRequired[
        "aws_sdk_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The ID of the Data Catalog where the partition in question resides. If none is provided, the Amazon Web Services account ID is used by default.</p>"""
    database_name: "aws_sdk_lakeformation.types.query_planning_context_database_name_string.QueryPlanningContextDatabaseNameString"
    """<p>The database containing the table.</p>"""
    query_as_of_time: NotRequired["aws_sdk_lakeformation.types.timestamp.Timestamp"]
    """<p>The time as of when to read the table contents. If not set, the most recent transaction commit time will be used. Cannot be specified along with <code>TransactionId</code>.</p>"""
    query_parameters: NotRequired[
        "aws_sdk_lakeformation.types.query_parameter_map.QueryParameterMap"
    ]
    """<p>A map consisting of key-value pairs.</p>"""
    transaction_id: NotRequired[
        "aws_sdk_lakeformation.types.transaction_id_string.TransactionIdString"
    ]
    """<p>The transaction ID at which to read the table contents. If this transaction is not committed, the read will be treated as part of that transaction and will see its writes. If this transaction has aborted, an error will be returned. If not set, defaults to the most recent committed transaction. Cannot be specified along with <code>QueryAsOfTime</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryPlanningContext) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    if "query_as_of_time" in value:
        import aws_sdk_lakeformation.types.timestamp

        out["QueryAsOfTime"] = aws_sdk_lakeformation.types.timestamp.serialize_json(
            value["query_as_of_time"]
        )
    if "query_parameters" in value:
        import aws_sdk_lakeformation.types.query_parameter_map

        out["QueryParameters"] = (
            aws_sdk_lakeformation.types.query_parameter_map.serialize_json(
                value["query_parameters"]
            )
        )
    if "transaction_id" in value:
        out["TransactionId"] = value["transaction_id"]
    return out


def deserialize_json(data: dict) -> QueryPlanningContext:
    out: QueryPlanningContext = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("QueryPlanningContext.database_name required")
    if "QueryAsOfTime" in data:
        import aws_sdk_lakeformation.types.timestamp

        out["query_as_of_time"] = (
            aws_sdk_lakeformation.types.timestamp.deserialize_json(
                data["QueryAsOfTime"]
            )
        )
    if "QueryParameters" in data:
        import aws_sdk_lakeformation.types.query_parameter_map

        out["query_parameters"] = (
            aws_sdk_lakeformation.types.query_parameter_map.deserialize_json(
                data["QueryParameters"]
            )
        )
    if "TransactionId" in data:
        out["transaction_id"] = data["TransactionId"]
    return out

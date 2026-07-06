"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowSQLTransformationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_integration_flow_sql_query


class DataIntegrationFlowSQLTransformationConfiguration(TypedDict, closed=True):
    query: "aws_sdk_supplychain.types.data_integration_flow_sql_query.DataIntegrationFlowSQLQuery"
    """<p>The transformation SQL query body based on SparkSQL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationFlowSQLTransformationConfiguration) -> dict:
    out: dict = {}
    out["query"] = value["query"]
    return out


def deserialize_json(data: dict) -> DataIntegrationFlowSQLTransformationConfiguration:
    out: DataIntegrationFlowSQLTransformationConfiguration = {}  # type: ignore[typeddict-item]
    if "query" in data:
        out["query"] = data["query"]
    else:
        raise DeserializationError(
            "DataIntegrationFlowSQLTransformationConfiguration.query required"
        )
    return out

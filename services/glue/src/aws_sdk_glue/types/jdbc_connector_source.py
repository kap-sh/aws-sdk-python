"""Generated from Smithy shape ``com.amazonaws.glue#JDBCConnectorSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.enclosed_in_string_property
    import aws_sdk_glue.types.enclosed_in_string_property_with_quote
    import aws_sdk_glue.types.glue_schemas
    import aws_sdk_glue.types.jdbc_connector_options
    import aws_sdk_glue.types.node_name
    import aws_sdk_glue.types.sql_query


class JDBCConnectorSource(TypedDict, closed=True):
    name: "aws_sdk_glue.types.node_name.NodeName"
    """<p>The name of the data source.</p>"""
    connection_name: (
        "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    )
    """<p>The name of the connection that is associated with the connector.</p>"""
    connector_name: (
        "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    )
    """<p>The name of a connector that assists with accessing the data store in Glue Studio.</p>"""
    connection_type: (
        "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    )
    """<p>The type of connection, such as marketplace.jdbc or custom.jdbc, designating a connection to a JDBC data store.</p>"""
    additional_options: NotRequired[
        "aws_sdk_glue.types.jdbc_connector_options.JDBCConnectorOptions"
    ]
    """<p>Additional connection options for the connector.</p>"""
    connection_table: NotRequired[
        "aws_sdk_glue.types.enclosed_in_string_property_with_quote.EnclosedInStringPropertyWithQuote"
    ]
    """<p>The name of the table in the data source.</p>"""
    query: NotRequired["aws_sdk_glue.types.sql_query.SqlQuery"]
    """<p>The table or SQL query to get the data from. You can specify either <code>ConnectionTable</code> or <code>query</code>, but not both.</p>"""
    output_schemas: NotRequired["aws_sdk_glue.types.glue_schemas.GlueSchemas"]
    """<p>Specifies the data schema for the custom JDBC source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JDBCConnectorSource) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["ConnectionName"] = value["connection_name"]
    out["ConnectorName"] = value["connector_name"]
    out["ConnectionType"] = value["connection_type"]
    if "additional_options" in value:
        import aws_sdk_glue.types.jdbc_connector_options

        out["AdditionalOptions"] = (
            aws_sdk_glue.types.jdbc_connector_options.serialize_aws_json_1_1(
                value["additional_options"]
            )
        )
    if "connection_table" in value:
        out["ConnectionTable"] = value["connection_table"]
    if "query" in value:
        out["Query"] = value["query"]
    if "output_schemas" in value:
        import aws_sdk_glue.types.glue_schemas

        out["OutputSchemas"] = aws_sdk_glue.types.glue_schemas.serialize_aws_json_1_1(
            value["output_schemas"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> JDBCConnectorSource:
    out: JDBCConnectorSource = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("JDBCConnectorSource.name required")
    if "ConnectionName" in data:
        out["connection_name"] = data["ConnectionName"]
    else:
        raise DeserializationError("JDBCConnectorSource.connection_name required")
    if "ConnectorName" in data:
        out["connector_name"] = data["ConnectorName"]
    else:
        raise DeserializationError("JDBCConnectorSource.connector_name required")
    if "ConnectionType" in data:
        out["connection_type"] = data["ConnectionType"]
    else:
        raise DeserializationError("JDBCConnectorSource.connection_type required")
    if "AdditionalOptions" in data:
        import aws_sdk_glue.types.jdbc_connector_options

        out["additional_options"] = (
            aws_sdk_glue.types.jdbc_connector_options.deserialize_aws_json_1_1(
                data["AdditionalOptions"]
            )
        )
    if "ConnectionTable" in data:
        out["connection_table"] = data["ConnectionTable"]
    if "Query" in data:
        out["query"] = data["Query"]
    if "OutputSchemas" in data:
        import aws_sdk_glue.types.glue_schemas

        out["output_schemas"] = (
            aws_sdk_glue.types.glue_schemas.deserialize_aws_json_1_1(
                data["OutputSchemas"]
            )
        )
    return out

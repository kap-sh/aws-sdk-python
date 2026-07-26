"""Generated from Smithy shape ``com.amazonaws.glue#JDBCConnectorTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.additional_options
    import capo_glue.types.enclosed_in_string_property
    import capo_glue.types.enclosed_in_string_property_with_quote
    import capo_glue.types.glue_schemas
    import capo_glue.types.node_name
    import capo_glue.types.one_input


class JDBCConnectorTarget(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of the data target.</p>"""
    inputs: "capo_glue.types.one_input.OneInput"
    """<p>The nodes that are inputs to the data target.</p>"""
    connection_name: (
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    )
    """<p>The name of the connection that is associated with the connector.</p>"""
    connection_table: "capo_glue.types.enclosed_in_string_property_with_quote.EnclosedInStringPropertyWithQuote"
    """<p>The name of the table in the data target.</p>"""
    connector_name: (
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    )
    """<p>The name of a connector that will be used.</p>"""
    connection_type: (
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    )
    """<p>The type of connection, such as marketplace.jdbc or custom.jdbc, designating a connection to a JDBC data target.</p>"""
    additional_options: NotRequired[
        "capo_glue.types.additional_options.AdditionalOptions"
    ]
    """<p>Additional connection options for the connector.</p>"""
    output_schemas: NotRequired["capo_glue.types.glue_schemas.GlueSchemas"]
    """<p>Specifies the data schema for the JDBC target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JDBCConnectorTarget) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_glue.types.one_input

    out["Inputs"] = capo_glue.types.one_input.serialize_aws_json_1_1(value["inputs"])
    out["ConnectionName"] = value["connection_name"]
    out["ConnectionTable"] = value["connection_table"]
    out["ConnectorName"] = value["connector_name"]
    out["ConnectionType"] = value["connection_type"]
    if "additional_options" in value:
        import capo_glue.types.additional_options

        out["AdditionalOptions"] = (
            capo_glue.types.additional_options.serialize_aws_json_1_1(
                value["additional_options"]
            )
        )
    if "output_schemas" in value:
        import capo_glue.types.glue_schemas

        out["OutputSchemas"] = capo_glue.types.glue_schemas.serialize_aws_json_1_1(
            value["output_schemas"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> JDBCConnectorTarget:
    out: JDBCConnectorTarget = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("JDBCConnectorTarget.name required")
    if "Inputs" in data:
        import capo_glue.types.one_input

        out["inputs"] = capo_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        raise DeserializationError("JDBCConnectorTarget.inputs required")
    if "ConnectionName" in data:
        out["connection_name"] = data["ConnectionName"]
    else:
        raise DeserializationError("JDBCConnectorTarget.connection_name required")
    if "ConnectionTable" in data:
        out["connection_table"] = data["ConnectionTable"]
    else:
        raise DeserializationError("JDBCConnectorTarget.connection_table required")
    if "ConnectorName" in data:
        out["connector_name"] = data["ConnectorName"]
    else:
        raise DeserializationError("JDBCConnectorTarget.connector_name required")
    if "ConnectionType" in data:
        out["connection_type"] = data["ConnectionType"]
    else:
        raise DeserializationError("JDBCConnectorTarget.connection_type required")
    if "AdditionalOptions" in data:
        import capo_glue.types.additional_options

        out["additional_options"] = (
            capo_glue.types.additional_options.deserialize_aws_json_1_1(
                data["AdditionalOptions"]
            )
        )
    if "OutputSchemas" in data:
        import capo_glue.types.glue_schemas

        out["output_schemas"] = capo_glue.types.glue_schemas.deserialize_aws_json_1_1(
            data["OutputSchemas"]
        )
    return out

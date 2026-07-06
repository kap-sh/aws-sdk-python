"""Generated from Smithy shape ``com.amazonaws.glue#SparkConnectorTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.additional_options
    import aws_sdk_glue.types.enclosed_in_string_property
    import aws_sdk_glue.types.glue_schemas
    import aws_sdk_glue.types.node_name
    import aws_sdk_glue.types.one_input


class SparkConnectorTarget(TypedDict, closed=True):
    name: "aws_sdk_glue.types.node_name.NodeName"
    """<p>The name of the data target.</p>"""
    inputs: "aws_sdk_glue.types.one_input.OneInput"
    """<p>The nodes that are inputs to the data target.</p>"""
    connection_name: (
        "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    )
    """<p>The name of a connection for an Apache Spark connector.</p>"""
    connector_name: (
        "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    )
    """<p>The name of an Apache Spark connector.</p>"""
    connection_type: (
        "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    )
    """<p>The type of connection, such as marketplace.spark or custom.spark, designating a connection to an Apache Spark data store.</p>"""
    additional_options: NotRequired[
        "aws_sdk_glue.types.additional_options.AdditionalOptions"
    ]
    """<p>Additional connection options for the connector.</p>"""
    output_schemas: NotRequired["aws_sdk_glue.types.glue_schemas.GlueSchemas"]
    """<p>Specifies the data schema for the custom spark target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SparkConnectorTarget) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_glue.types.one_input

    out["Inputs"] = aws_sdk_glue.types.one_input.serialize_aws_json_1_1(value["inputs"])
    out["ConnectionName"] = value["connection_name"]
    out["ConnectorName"] = value["connector_name"]
    out["ConnectionType"] = value["connection_type"]
    if "additional_options" in value:
        import aws_sdk_glue.types.additional_options

        out["AdditionalOptions"] = (
            aws_sdk_glue.types.additional_options.serialize_aws_json_1_1(
                value["additional_options"]
            )
        )
    if "output_schemas" in value:
        import aws_sdk_glue.types.glue_schemas

        out["OutputSchemas"] = aws_sdk_glue.types.glue_schemas.serialize_aws_json_1_1(
            value["output_schemas"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SparkConnectorTarget:
    out: SparkConnectorTarget = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("SparkConnectorTarget.name required")
    if "Inputs" in data:
        import aws_sdk_glue.types.one_input

        out["inputs"] = aws_sdk_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        raise DeserializationError("SparkConnectorTarget.inputs required")
    if "ConnectionName" in data:
        out["connection_name"] = data["ConnectionName"]
    else:
        raise DeserializationError("SparkConnectorTarget.connection_name required")
    if "ConnectorName" in data:
        out["connector_name"] = data["ConnectorName"]
    else:
        raise DeserializationError("SparkConnectorTarget.connector_name required")
    if "ConnectionType" in data:
        out["connection_type"] = data["ConnectionType"]
    else:
        raise DeserializationError("SparkConnectorTarget.connection_type required")
    if "AdditionalOptions" in data:
        import aws_sdk_glue.types.additional_options

        out["additional_options"] = (
            aws_sdk_glue.types.additional_options.deserialize_aws_json_1_1(
                data["AdditionalOptions"]
            )
        )
    if "OutputSchemas" in data:
        import aws_sdk_glue.types.glue_schemas

        out["output_schemas"] = (
            aws_sdk_glue.types.glue_schemas.deserialize_aws_json_1_1(
                data["OutputSchemas"]
            )
        )
    return out

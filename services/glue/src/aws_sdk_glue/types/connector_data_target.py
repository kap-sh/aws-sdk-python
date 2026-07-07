"""Generated from Smithy shape ``com.amazonaws.glue#ConnectorDataTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.connector_options
    import aws_sdk_glue.types.enclosed_in_string_property
    import aws_sdk_glue.types.node_name
    import aws_sdk_glue.types.one_input


class ConnectorDataTarget(TypedDict, closed=True):
    name: "aws_sdk_glue.types.node_name.NodeName"
    """<p>The name of this target node.</p>"""
    connection_type: (
        "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    )
    """<p>The <code>connectionType</code>, as provided to the underlying Glue library. This node type supports the following connection types: </p> <ul> <li> <p> <code>opensearch</code> </p> </li> <li> <p> <code>azuresql</code> </p> </li> <li> <p> <code>azurecosmos</code> </p> </li> <li> <p> <code>bigquery</code> </p> </li> <li> <p> <code>saphana</code> </p> </li> <li> <p> <code>teradata</code> </p> </li> <li> <p> <code>vertica</code> </p> </li> </ul>"""
    data: "aws_sdk_glue.types.connector_options.ConnectorOptions"
    r"""<p>A map specifying connection options for the node. You can find standard connection options for the corresponding connection type in the <a href=\"https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-connect.html\"> Connection parameters</a> section of the Glue documentation.</p>"""
    inputs: NotRequired["aws_sdk_glue.types.one_input.OneInput"]
    """<p>The nodes that are inputs to the data target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectorDataTarget) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["ConnectionType"] = value["connection_type"]
    import aws_sdk_glue.types.connector_options

    out["Data"] = aws_sdk_glue.types.connector_options.serialize_aws_json_1_1(
        value["data"]
    )
    if "inputs" in value:
        import aws_sdk_glue.types.one_input

        out["Inputs"] = aws_sdk_glue.types.one_input.serialize_aws_json_1_1(
            value["inputs"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectorDataTarget:
    out: ConnectorDataTarget = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ConnectorDataTarget.name required")
    if "ConnectionType" in data:
        out["connection_type"] = data["ConnectionType"]
    else:
        raise DeserializationError("ConnectorDataTarget.connection_type required")
    if "Data" in data:
        import aws_sdk_glue.types.connector_options

        out["data"] = aws_sdk_glue.types.connector_options.deserialize_aws_json_1_1(
            data["Data"]
        )
    else:
        raise DeserializationError("ConnectorDataTarget.data required")
    if "Inputs" in data:
        import aws_sdk_glue.types.one_input

        out["inputs"] = aws_sdk_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    return out

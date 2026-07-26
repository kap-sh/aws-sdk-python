"""Generated from Smithy shape ``com.amazonaws.glue#DynamoDBELTConnectorSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.ddbelt_connection_options
    import capo_glue.types.glue_schemas
    import capo_glue.types.node_name


class DynamoDBELTConnectorSource(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of the DynamoDB ELT connector source.</p>"""
    connection_options: NotRequired[
        "capo_glue.types.ddbelt_connection_options.DDBELTConnectionOptions"
    ]
    """<p>The connection options for the DynamoDB ELT connector source.</p>"""
    output_schemas: NotRequired["capo_glue.types.glue_schemas.GlueSchemas"]
    """<p>Specifies the data schema for the DynamoDB ELT connector source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DynamoDBELTConnectorSource) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "connection_options" in value:
        import capo_glue.types.ddbelt_connection_options

        out["ConnectionOptions"] = (
            capo_glue.types.ddbelt_connection_options.serialize_aws_json_1_1(
                value["connection_options"]
            )
        )
    if "output_schemas" in value:
        import capo_glue.types.glue_schemas

        out["OutputSchemas"] = capo_glue.types.glue_schemas.serialize_aws_json_1_1(
            value["output_schemas"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DynamoDBELTConnectorSource:
    out: DynamoDBELTConnectorSource = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DynamoDBELTConnectorSource.name required")
    if "ConnectionOptions" in data:
        import capo_glue.types.ddbelt_connection_options

        out["connection_options"] = (
            capo_glue.types.ddbelt_connection_options.deserialize_aws_json_1_1(
                data["ConnectionOptions"]
            )
        )
    if "OutputSchemas" in data:
        import capo_glue.types.glue_schemas

        out["output_schemas"] = capo_glue.types.glue_schemas.deserialize_aws_json_1_1(
            data["OutputSchemas"]
        )
    return out

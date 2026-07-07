"""Generated from Smithy shape ``com.amazonaws.glue#DynamoDBCatalogSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.boxed_boolean
    import aws_sdk_glue.types.ddbelt_catalog_additional_options
    import aws_sdk_glue.types.enclosed_in_string_property
    import aws_sdk_glue.types.node_name


class DynamoDBCatalogSource(TypedDict, closed=True):
    name: "aws_sdk_glue.types.node_name.NodeName"
    """<p>The name of the data source.</p>"""
    database: "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The name of the database to read from.</p>"""
    table: "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The name of the table in the database to read from.</p>"""
    pitr_enabled: NotRequired["aws_sdk_glue.types.boxed_boolean.BoxedBoolean"]
    """<p>Specifies whether Point-in-Time Recovery (PITR) is enabled for the DynamoDB table. When set to <code>true</code>, allows reading from a specific point in time. The default value is <code>false</code>.</p>"""
    additional_options: NotRequired[
        "aws_sdk_glue.types.ddbelt_catalog_additional_options.DDBELTCatalogAdditionalOptions"
    ]
    """<p>Specifies additional connection options for the DynamoDB data source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DynamoDBCatalogSource) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Database"] = value["database"]
    out["Table"] = value["table"]
    if "pitr_enabled" in value:
        out["PitrEnabled"] = value["pitr_enabled"]
    if "additional_options" in value:
        import aws_sdk_glue.types.ddbelt_catalog_additional_options

        out["AdditionalOptions"] = (
            aws_sdk_glue.types.ddbelt_catalog_additional_options.serialize_aws_json_1_1(
                value["additional_options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DynamoDBCatalogSource:
    out: DynamoDBCatalogSource = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DynamoDBCatalogSource.name required")
    if "Database" in data:
        out["database"] = data["Database"]
    else:
        raise DeserializationError("DynamoDBCatalogSource.database required")
    if "Table" in data:
        out["table"] = data["Table"]
    else:
        raise DeserializationError("DynamoDBCatalogSource.table required")
    if "PitrEnabled" in data:
        out["pitr_enabled"] = data["PitrEnabled"]
    if "AdditionalOptions" in data:
        import aws_sdk_glue.types.ddbelt_catalog_additional_options

        out["additional_options"] = (
            aws_sdk_glue.types.ddbelt_catalog_additional_options.deserialize_aws_json_1_1(
                data["AdditionalOptions"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.glue#DirectJDBCSource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.enclosed_in_string_property
    import aws_sdk_glue.types.glue_schemas
    import aws_sdk_glue.types.jdbc_connection_type
    import aws_sdk_glue.types.node_name


class DirectJDBCSource(TypedDict):
    name: "aws_sdk_glue.types.node_name.NodeName"
    """<p>The name of the JDBC source connection.</p>"""
    database: "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The database of the JDBC source connection.</p>"""
    table: "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The table of the JDBC source connection.</p>"""
    connection_name: (
        "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    )
    """<p>The connection name of the JDBC source.</p>"""
    connection_type: "aws_sdk_glue.types.jdbc_connection_type.JDBCConnectionType"
    """<p>The connection type of the JDBC source.</p>"""
    redshift_tmp_dir: NotRequired[
        "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>The temp directory of the JDBC Redshift source.</p>"""
    output_schemas: NotRequired["aws_sdk_glue.types.glue_schemas.GlueSchemas"]
    """<p>Specifies the data schema for the direct JDBC source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectJDBCSource) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Database"] = value["database"]
    out["Table"] = value["table"]
    out["ConnectionName"] = value["connection_name"]
    import aws_sdk_glue.types.jdbc_connection_type

    out["ConnectionType"] = (
        aws_sdk_glue.types.jdbc_connection_type.serialize_aws_json_1_1(
            value["connection_type"]
        )
    )
    if "redshift_tmp_dir" in value:
        out["RedshiftTmpDir"] = value["redshift_tmp_dir"]
    if "output_schemas" in value:
        import aws_sdk_glue.types.glue_schemas

        out["OutputSchemas"] = aws_sdk_glue.types.glue_schemas.serialize_aws_json_1_1(
            value["output_schemas"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DirectJDBCSource:
    out: DirectJDBCSource = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DirectJDBCSource.name required")
    if "Database" in data:
        out["database"] = data["Database"]
    else:
        raise DeserializationError("DirectJDBCSource.database required")
    if "Table" in data:
        out["table"] = data["Table"]
    else:
        raise DeserializationError("DirectJDBCSource.table required")
    if "ConnectionName" in data:
        out["connection_name"] = data["ConnectionName"]
    else:
        raise DeserializationError("DirectJDBCSource.connection_name required")
    if "ConnectionType" in data:
        import aws_sdk_glue.types.jdbc_connection_type

        out["connection_type"] = (
            aws_sdk_glue.types.jdbc_connection_type.deserialize_aws_json_1_1(
                data["ConnectionType"]
            )
        )
    else:
        raise DeserializationError("DirectJDBCSource.connection_type required")
    if "RedshiftTmpDir" in data:
        out["redshift_tmp_dir"] = data["RedshiftTmpDir"]
    if "OutputSchemas" in data:
        import aws_sdk_glue.types.glue_schemas

        out["output_schemas"] = (
            aws_sdk_glue.types.glue_schemas.deserialize_aws_json_1_1(
                data["OutputSchemas"]
            )
        )
    return out

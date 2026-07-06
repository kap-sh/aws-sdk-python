"""Generated from Smithy shape ``com.amazonaws.glue#PostgreSQLCatalogTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.enclosed_in_string_property
    import aws_sdk_glue.types.node_name
    import aws_sdk_glue.types.one_input


class PostgreSQLCatalogTarget(TypedDict, closed=True):
    name: "aws_sdk_glue.types.node_name.NodeName"
    """<p>The name of the data target.</p>"""
    inputs: "aws_sdk_glue.types.one_input.OneInput"
    """<p>The nodes that are inputs to the data target.</p>"""
    database: "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The name of the database to write to.</p>"""
    table: "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The name of the table in the database to write to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PostgreSQLCatalogTarget) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_glue.types.one_input

    out["Inputs"] = aws_sdk_glue.types.one_input.serialize_aws_json_1_1(value["inputs"])
    out["Database"] = value["database"]
    out["Table"] = value["table"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PostgreSQLCatalogTarget:
    out: PostgreSQLCatalogTarget = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("PostgreSQLCatalogTarget.name required")
    if "Inputs" in data:
        import aws_sdk_glue.types.one_input

        out["inputs"] = aws_sdk_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        raise DeserializationError("PostgreSQLCatalogTarget.inputs required")
    if "Database" in data:
        out["database"] = data["Database"]
    else:
        raise DeserializationError("PostgreSQLCatalogTarget.database required")
    if "Table" in data:
        out["table"] = data["Table"]
    else:
        raise DeserializationError("PostgreSQLCatalogTarget.table required")
    return out

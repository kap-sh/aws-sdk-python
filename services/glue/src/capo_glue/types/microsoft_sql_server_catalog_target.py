"""Generated from Smithy shape ``com.amazonaws.glue#MicrosoftSQLServerCatalogTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.enclosed_in_string_property
    import capo_glue.types.node_name
    import capo_glue.types.one_input


class MicrosoftSQLServerCatalogTarget(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of the data target.</p>"""
    inputs: "capo_glue.types.one_input.OneInput"
    """<p>The nodes that are inputs to the data target.</p>"""
    database: "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The name of the database to write to.</p>"""
    table: "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The name of the table in the database to write to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MicrosoftSQLServerCatalogTarget) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_glue.types.one_input

    out["Inputs"] = capo_glue.types.one_input.serialize_aws_json_1_1(value["inputs"])
    out["Database"] = value["database"]
    out["Table"] = value["table"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MicrosoftSQLServerCatalogTarget:
    out: MicrosoftSQLServerCatalogTarget = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("MicrosoftSQLServerCatalogTarget.name required")
    if "Inputs" in data:
        import capo_glue.types.one_input

        out["inputs"] = capo_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        raise DeserializationError("MicrosoftSQLServerCatalogTarget.inputs required")
    if "Database" in data:
        out["database"] = data["Database"]
    else:
        raise DeserializationError("MicrosoftSQLServerCatalogTarget.database required")
    if "Table" in data:
        out["table"] = data["Table"]
    else:
        raise DeserializationError("MicrosoftSQLServerCatalogTarget.table required")
    return out

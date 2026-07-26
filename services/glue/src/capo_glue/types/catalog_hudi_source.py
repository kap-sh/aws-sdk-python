"""Generated from Smithy shape ``com.amazonaws.glue#CatalogHudiSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.additional_options
    import capo_glue.types.enclosed_in_string_property
    import capo_glue.types.glue_schemas
    import capo_glue.types.node_name


class CatalogHudiSource(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of the Hudi data source.</p>"""
    database: "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The name of the database to read from.</p>"""
    table: "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The name of the table in the database to read from.</p>"""
    additional_hudi_options: NotRequired[
        "capo_glue.types.additional_options.AdditionalOptions"
    ]
    """<p>Specifies additional connection options.</p>"""
    output_schemas: NotRequired["capo_glue.types.glue_schemas.GlueSchemas"]
    """<p>Specifies the data schema for the Hudi source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CatalogHudiSource) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Database"] = value["database"]
    out["Table"] = value["table"]
    if "additional_hudi_options" in value:
        import capo_glue.types.additional_options

        out["AdditionalHudiOptions"] = (
            capo_glue.types.additional_options.serialize_aws_json_1_1(
                value["additional_hudi_options"]
            )
        )
    if "output_schemas" in value:
        import capo_glue.types.glue_schemas

        out["OutputSchemas"] = capo_glue.types.glue_schemas.serialize_aws_json_1_1(
            value["output_schemas"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CatalogHudiSource:
    out: CatalogHudiSource = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CatalogHudiSource.name required")
    if "Database" in data:
        out["database"] = data["Database"]
    else:
        raise DeserializationError("CatalogHudiSource.database required")
    if "Table" in data:
        out["table"] = data["Table"]
    else:
        raise DeserializationError("CatalogHudiSource.table required")
    if "AdditionalHudiOptions" in data:
        import capo_glue.types.additional_options

        out["additional_hudi_options"] = (
            capo_glue.types.additional_options.deserialize_aws_json_1_1(
                data["AdditionalHudiOptions"]
            )
        )
    if "OutputSchemas" in data:
        import capo_glue.types.glue_schemas

        out["output_schemas"] = capo_glue.types.glue_schemas.deserialize_aws_json_1_1(
            data["OutputSchemas"]
        )
    return out

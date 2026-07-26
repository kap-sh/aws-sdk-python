"""Generated from Smithy shape ``com.amazonaws.databrew#Input``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.data_catalog_input_definition
    import capo_databrew.types.database_input_definition
    import capo_databrew.types.metadata
    import capo_databrew.types.s3_location


class Input(TypedDict, closed=True):
    s3_input_definition: NotRequired["capo_databrew.types.s3_location.S3Location"]
    """<p>The Amazon S3 location where the data is stored.</p>"""
    data_catalog_input_definition: NotRequired[
        "capo_databrew.types.data_catalog_input_definition.DataCatalogInputDefinition"
    ]
    """<p>The Glue Data Catalog parameters for the data.</p>"""
    database_input_definition: NotRequired[
        "capo_databrew.types.database_input_definition.DatabaseInputDefinition"
    ]
    """<p>Connection information for dataset input files stored in a database.</p>"""
    metadata: NotRequired["capo_databrew.types.metadata.Metadata"]
    """<p>Contains additional resource information needed for specific datasets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Input) -> dict:
    out: dict = {}
    if "s3_input_definition" in value:
        import capo_databrew.types.s3_location

        out["S3InputDefinition"] = capo_databrew.types.s3_location.serialize_json(
            value["s3_input_definition"]
        )
    if "data_catalog_input_definition" in value:
        import capo_databrew.types.data_catalog_input_definition

        out["DataCatalogInputDefinition"] = (
            capo_databrew.types.data_catalog_input_definition.serialize_json(
                value["data_catalog_input_definition"]
            )
        )
    if "database_input_definition" in value:
        import capo_databrew.types.database_input_definition

        out["DatabaseInputDefinition"] = (
            capo_databrew.types.database_input_definition.serialize_json(
                value["database_input_definition"]
            )
        )
    if "metadata" in value:
        import capo_databrew.types.metadata

        out["Metadata"] = capo_databrew.types.metadata.serialize_json(value["metadata"])
    return out


def deserialize_json(data: dict) -> Input:
    out: Input = {}  # type: ignore[typeddict-item]
    if "S3InputDefinition" in data:
        import capo_databrew.types.s3_location

        out["s3_input_definition"] = capo_databrew.types.s3_location.deserialize_json(
            data["S3InputDefinition"]
        )
    if "DataCatalogInputDefinition" in data:
        import capo_databrew.types.data_catalog_input_definition

        out["data_catalog_input_definition"] = (
            capo_databrew.types.data_catalog_input_definition.deserialize_json(
                data["DataCatalogInputDefinition"]
            )
        )
    if "DatabaseInputDefinition" in data:
        import capo_databrew.types.database_input_definition

        out["database_input_definition"] = (
            capo_databrew.types.database_input_definition.deserialize_json(
                data["DatabaseInputDefinition"]
            )
        )
    if "Metadata" in data:
        import capo_databrew.types.metadata

        out["metadata"] = capo_databrew.types.metadata.deserialize_json(
            data["Metadata"]
        )
    return out

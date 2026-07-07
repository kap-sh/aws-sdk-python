"""Generated from Smithy shape ``com.amazonaws.databrew#Input``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_databrew.types.data_catalog_input_definition
    import aws_sdk_databrew.types.database_input_definition
    import aws_sdk_databrew.types.metadata
    import aws_sdk_databrew.types.s3_location


class Input(TypedDict, closed=True):
    s3_input_definition: NotRequired["aws_sdk_databrew.types.s3_location.S3Location"]
    """<p>The Amazon S3 location where the data is stored.</p>"""
    data_catalog_input_definition: NotRequired[
        "aws_sdk_databrew.types.data_catalog_input_definition.DataCatalogInputDefinition"
    ]
    """<p>The Glue Data Catalog parameters for the data.</p>"""
    database_input_definition: NotRequired[
        "aws_sdk_databrew.types.database_input_definition.DatabaseInputDefinition"
    ]
    """<p>Connection information for dataset input files stored in a database.</p>"""
    metadata: NotRequired["aws_sdk_databrew.types.metadata.Metadata"]
    """<p>Contains additional resource information needed for specific datasets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Input) -> dict:
    out: dict = {}
    if "s3_input_definition" in value:
        import aws_sdk_databrew.types.s3_location

        out["S3InputDefinition"] = aws_sdk_databrew.types.s3_location.serialize_json(
            value["s3_input_definition"]
        )
    if "data_catalog_input_definition" in value:
        import aws_sdk_databrew.types.data_catalog_input_definition

        out["DataCatalogInputDefinition"] = (
            aws_sdk_databrew.types.data_catalog_input_definition.serialize_json(
                value["data_catalog_input_definition"]
            )
        )
    if "database_input_definition" in value:
        import aws_sdk_databrew.types.database_input_definition

        out["DatabaseInputDefinition"] = (
            aws_sdk_databrew.types.database_input_definition.serialize_json(
                value["database_input_definition"]
            )
        )
    if "metadata" in value:
        import aws_sdk_databrew.types.metadata

        out["Metadata"] = aws_sdk_databrew.types.metadata.serialize_json(
            value["metadata"]
        )
    return out


def deserialize_json(data: dict) -> Input:
    out: Input = {}  # type: ignore[typeddict-item]
    if "S3InputDefinition" in data:
        import aws_sdk_databrew.types.s3_location

        out["s3_input_definition"] = (
            aws_sdk_databrew.types.s3_location.deserialize_json(
                data["S3InputDefinition"]
            )
        )
    if "DataCatalogInputDefinition" in data:
        import aws_sdk_databrew.types.data_catalog_input_definition

        out["data_catalog_input_definition"] = (
            aws_sdk_databrew.types.data_catalog_input_definition.deserialize_json(
                data["DataCatalogInputDefinition"]
            )
        )
    if "DatabaseInputDefinition" in data:
        import aws_sdk_databrew.types.database_input_definition

        out["database_input_definition"] = (
            aws_sdk_databrew.types.database_input_definition.deserialize_json(
                data["DatabaseInputDefinition"]
            )
        )
    if "Metadata" in data:
        import aws_sdk_databrew.types.metadata

        out["metadata"] = aws_sdk_databrew.types.metadata.deserialize_json(
            data["Metadata"]
        )
    return out

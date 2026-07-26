"""Generated from Smithy shape ``com.amazonaws.appflow#MetadataCatalogDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.catalog_type
    import capo_appflow.types.registration_output
    import capo_appflow.types.string


class MetadataCatalogDetail(TypedDict, closed=True):
    catalog_type: NotRequired["capo_appflow.types.catalog_type.CatalogType"]
    """<p>The type of metadata catalog that Amazon AppFlow used for the associated flow run. This parameter returns the following value:</p> <dl> <dt>GLUE</dt> <dd> <p>The metadata catalog is provided by the Glue Data Catalog. Glue includes the Glue Data Catalog as a component.</p> </dd> </dl>"""
    table_name: NotRequired["capo_appflow.types.string.String"]
    """<p>The name of the table that stores the metadata for the associated flow run. The table stores metadata that represents the data that the flow transferred. Amazon AppFlow stores the table in the metadata catalog.</p>"""
    table_registration_output: NotRequired[
        "capo_appflow.types.registration_output.RegistrationOutput"
    ]
    """<p>Describes the status of the attempt from Amazon AppFlow to register the metadata table with the metadata catalog. Amazon AppFlow creates or updates this table for the associated flow run.</p>"""
    partition_registration_output: NotRequired[
        "capo_appflow.types.registration_output.RegistrationOutput"
    ]
    """<p>Describes the status of the attempt from Amazon AppFlow to register the data partitions with the metadata catalog. The data partitions organize the flow output into a hierarchical path, such as a folder path in an S3 bucket. Amazon AppFlow creates the partitions (if they don't already exist) based on your flow configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetadataCatalogDetail) -> dict:
    out: dict = {}
    if "catalog_type" in value:
        import capo_appflow.types.catalog_type

        out["catalogType"] = capo_appflow.types.catalog_type.serialize_json(
            value["catalog_type"]
        )
    if "table_name" in value:
        out["tableName"] = value["table_name"]
    if "table_registration_output" in value:
        import capo_appflow.types.registration_output

        out["tableRegistrationOutput"] = (
            capo_appflow.types.registration_output.serialize_json(
                value["table_registration_output"]
            )
        )
    if "partition_registration_output" in value:
        import capo_appflow.types.registration_output

        out["partitionRegistrationOutput"] = (
            capo_appflow.types.registration_output.serialize_json(
                value["partition_registration_output"]
            )
        )
    return out


def deserialize_json(data: dict) -> MetadataCatalogDetail:
    out: MetadataCatalogDetail = {}  # type: ignore[typeddict-item]
    if "catalogType" in data:
        import capo_appflow.types.catalog_type

        out["catalog_type"] = capo_appflow.types.catalog_type.deserialize_json(
            data["catalogType"]
        )
    if "tableName" in data:
        out["table_name"] = data["tableName"]
    if "tableRegistrationOutput" in data:
        import capo_appflow.types.registration_output

        out["table_registration_output"] = (
            capo_appflow.types.registration_output.deserialize_json(
                data["tableRegistrationOutput"]
            )
        )
    if "partitionRegistrationOutput" in data:
        import capo_appflow.types.registration_output

        out["partition_registration_output"] = (
            capo_appflow.types.registration_output.deserialize_json(
                data["partitionRegistrationOutput"]
            )
        )
    return out

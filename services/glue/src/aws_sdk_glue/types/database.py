"""Generated from Smithy shape ``com.amazonaws.glue#Database``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.catalog_id_string
    import aws_sdk_glue.types.database_identifier
    import aws_sdk_glue.types.description_string
    import aws_sdk_glue.types.federated_database
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.parameters_map
    import aws_sdk_glue.types.principal_permissions_list
    import aws_sdk_glue.types.timestamp
    import aws_sdk_glue.types.uri


class Database(TypedDict, closed=True):
    name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the database. For Hive compatibility, this is folded to lowercase when it is stored.</p>"""
    description: NotRequired["aws_sdk_glue.types.description_string.DescriptionString"]
    """<p>A description of the database.</p>"""
    location_uri: NotRequired["aws_sdk_glue.types.uri.URI"]
    """<p>The location of the database (for example, an HDFS path).</p>"""
    parameters: NotRequired["aws_sdk_glue.types.parameters_map.ParametersMap"]
    """<p>These key-value pairs define parameters and properties of the database.</p>"""
    create_time: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The time at which the metadata database was created in the catalog.</p>"""
    create_table_default_permissions: NotRequired[
        "aws_sdk_glue.types.principal_permissions_list.PrincipalPermissionsList"
    ]
    """<p>Creates a set of default permissions on the table for principals. Used by Lake Formation. Not used in the normal course of Glue operations.</p>"""
    target_database: NotRequired[
        "aws_sdk_glue.types.database_identifier.DatabaseIdentifier"
    ]
    """<p>A <code>DatabaseIdentifier</code> structure that describes a target database for resource linking.</p>"""
    catalog_id: NotRequired["aws_sdk_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog in which the database resides.</p>"""
    federated_database: NotRequired[
        "aws_sdk_glue.types.federated_database.FederatedDatabase"
    ]
    """<p>A <code>FederatedDatabase</code> structure that references an entity outside the Glue Data Catalog.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Database) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "location_uri" in value:
        out["LocationUri"] = value["location_uri"]
    if "parameters" in value:
        import aws_sdk_glue.types.parameters_map

        out["Parameters"] = aws_sdk_glue.types.parameters_map.serialize_aws_json_1_1(
            value["parameters"]
        )
    if "create_time" in value:
        import aws_sdk_glue.types.timestamp

        out["CreateTime"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["create_time"]
        )
    if "create_table_default_permissions" in value:
        import aws_sdk_glue.types.principal_permissions_list

        out["CreateTableDefaultPermissions"] = (
            aws_sdk_glue.types.principal_permissions_list.serialize_aws_json_1_1(
                value["create_table_default_permissions"]
            )
        )
    if "target_database" in value:
        import aws_sdk_glue.types.database_identifier

        out["TargetDatabase"] = (
            aws_sdk_glue.types.database_identifier.serialize_aws_json_1_1(
                value["target_database"]
            )
        )
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    if "federated_database" in value:
        import aws_sdk_glue.types.federated_database

        out["FederatedDatabase"] = (
            aws_sdk_glue.types.federated_database.serialize_aws_json_1_1(
                value["federated_database"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Database:
    out: Database = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Database.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "LocationUri" in data:
        out["location_uri"] = data["LocationUri"]
    if "Parameters" in data:
        import aws_sdk_glue.types.parameters_map

        out["parameters"] = aws_sdk_glue.types.parameters_map.deserialize_aws_json_1_1(
            data["Parameters"]
        )
    if "CreateTime" in data:
        import aws_sdk_glue.types.timestamp

        out["create_time"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["CreateTime"]
        )
    if "CreateTableDefaultPermissions" in data:
        import aws_sdk_glue.types.principal_permissions_list

        out["create_table_default_permissions"] = (
            aws_sdk_glue.types.principal_permissions_list.deserialize_aws_json_1_1(
                data["CreateTableDefaultPermissions"]
            )
        )
    if "TargetDatabase" in data:
        import aws_sdk_glue.types.database_identifier

        out["target_database"] = (
            aws_sdk_glue.types.database_identifier.deserialize_aws_json_1_1(
                data["TargetDatabase"]
            )
        )
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "FederatedDatabase" in data:
        import aws_sdk_glue.types.federated_database

        out["federated_database"] = (
            aws_sdk_glue.types.federated_database.deserialize_aws_json_1_1(
                data["FederatedDatabase"]
            )
        )
    return out

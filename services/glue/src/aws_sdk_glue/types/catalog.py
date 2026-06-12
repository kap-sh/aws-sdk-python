"""Generated from Smithy shape ``com.amazonaws.glue#Catalog``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.allow_full_table_external_data_access_enum
    import aws_sdk_glue.types.catalog_id_string
    import aws_sdk_glue.types.catalog_name_string
    import aws_sdk_glue.types.catalog_properties_output
    import aws_sdk_glue.types.description_string
    import aws_sdk_glue.types.federated_catalog
    import aws_sdk_glue.types.parameters_map
    import aws_sdk_glue.types.principal_permissions_list
    import aws_sdk_glue.types.resource_arn_string
    import aws_sdk_glue.types.target_redshift_catalog
    import aws_sdk_glue.types.timestamp


class Catalog(TypedDict):
    catalog_id: NotRequired["aws_sdk_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the catalog. To grant access to the default catalog, this field should not be provided.</p>"""
    name: "aws_sdk_glue.types.catalog_name_string.CatalogNameString"
    """<p>The name of the catalog. Cannot be the same as the account ID.</p>"""
    resource_arn: NotRequired[
        "aws_sdk_glue.types.resource_arn_string.ResourceArnString"
    ]
    """<p>The Amazon Resource Name (ARN) assigned to the catalog resource.</p>"""
    description: NotRequired["aws_sdk_glue.types.description_string.DescriptionString"]
    """<p>Description string, not more than 2048 bytes long, matching the URI address multi-line string pattern. A description of the catalog.</p>"""
    parameters: NotRequired["aws_sdk_glue.types.parameters_map.ParametersMap"]
    """<p> A map array of key-value pairs that define parameters and properties of the catalog.</p>"""
    create_time: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The time at which the catalog was created.</p>"""
    update_time: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The time at which the catalog was last updated.</p>"""
    target_redshift_catalog: NotRequired[
        "aws_sdk_glue.types.target_redshift_catalog.TargetRedshiftCatalog"
    ]
    """<p>A <code>TargetRedshiftCatalog</code> object that describes a target catalog for database resource linking.</p>"""
    federated_catalog: NotRequired[
        "aws_sdk_glue.types.federated_catalog.FederatedCatalog"
    ]
    """<p>A <code>FederatedCatalog</code> object that points to an entity outside the Glue Data Catalog.</p>"""
    catalog_properties: NotRequired[
        "aws_sdk_glue.types.catalog_properties_output.CatalogPropertiesOutput"
    ]
    """<p>A <code>CatalogProperties</code> object that specifies data lake access properties and other custom properties.</p>"""
    create_table_default_permissions: NotRequired[
        "aws_sdk_glue.types.principal_permissions_list.PrincipalPermissionsList"
    ]
    """<p>An array of <code>PrincipalPermissions</code> objects. Creates a set of default permissions on the table(s) for principals. Used by Amazon Web Services Lake Formation. Not used in the normal course of Glue operations.</p>"""
    create_database_default_permissions: NotRequired[
        "aws_sdk_glue.types.principal_permissions_list.PrincipalPermissionsList"
    ]
    """<p>An array of <code>PrincipalPermissions</code> objects. Creates a set of default permissions on the database(s) for principals. Used by Amazon Web Services Lake Formation. Not used in the normal course of Glue operations.</p>"""
    allow_full_table_external_data_access: NotRequired[
        "aws_sdk_glue.types.allow_full_table_external_data_access_enum.AllowFullTableExternalDataAccessEnum"
    ]
    """<p> Allows third-party engines to access data in Amazon S3 locations that are registered with Lake Formation. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Catalog) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["Name"] = value["name"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "description" in value:
        out["Description"] = value["description"]
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
    if "update_time" in value:
        import aws_sdk_glue.types.timestamp

        out["UpdateTime"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["update_time"]
        )
    if "target_redshift_catalog" in value:
        import aws_sdk_glue.types.target_redshift_catalog

        out["TargetRedshiftCatalog"] = (
            aws_sdk_glue.types.target_redshift_catalog.serialize_aws_json_1_1(
                value["target_redshift_catalog"]
            )
        )
    if "federated_catalog" in value:
        import aws_sdk_glue.types.federated_catalog

        out["FederatedCatalog"] = (
            aws_sdk_glue.types.federated_catalog.serialize_aws_json_1_1(
                value["federated_catalog"]
            )
        )
    if "catalog_properties" in value:
        import aws_sdk_glue.types.catalog_properties_output

        out["CatalogProperties"] = (
            aws_sdk_glue.types.catalog_properties_output.serialize_aws_json_1_1(
                value["catalog_properties"]
            )
        )
    if "create_table_default_permissions" in value:
        import aws_sdk_glue.types.principal_permissions_list

        out["CreateTableDefaultPermissions"] = (
            aws_sdk_glue.types.principal_permissions_list.serialize_aws_json_1_1(
                value["create_table_default_permissions"]
            )
        )
    if "create_database_default_permissions" in value:
        import aws_sdk_glue.types.principal_permissions_list

        out["CreateDatabaseDefaultPermissions"] = (
            aws_sdk_glue.types.principal_permissions_list.serialize_aws_json_1_1(
                value["create_database_default_permissions"]
            )
        )
    if "allow_full_table_external_data_access" in value:
        import aws_sdk_glue.types.allow_full_table_external_data_access_enum

        out["AllowFullTableExternalDataAccess"] = (
            aws_sdk_glue.types.allow_full_table_external_data_access_enum.serialize_aws_json_1_1(
                value["allow_full_table_external_data_access"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Catalog:
    out: Catalog = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Catalog.name required")
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "Description" in data:
        out["description"] = data["Description"]
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
    if "UpdateTime" in data:
        import aws_sdk_glue.types.timestamp

        out["update_time"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["UpdateTime"]
        )
    if "TargetRedshiftCatalog" in data:
        import aws_sdk_glue.types.target_redshift_catalog

        out["target_redshift_catalog"] = (
            aws_sdk_glue.types.target_redshift_catalog.deserialize_aws_json_1_1(
                data["TargetRedshiftCatalog"]
            )
        )
    if "FederatedCatalog" in data:
        import aws_sdk_glue.types.federated_catalog

        out["federated_catalog"] = (
            aws_sdk_glue.types.federated_catalog.deserialize_aws_json_1_1(
                data["FederatedCatalog"]
            )
        )
    if "CatalogProperties" in data:
        import aws_sdk_glue.types.catalog_properties_output

        out["catalog_properties"] = (
            aws_sdk_glue.types.catalog_properties_output.deserialize_aws_json_1_1(
                data["CatalogProperties"]
            )
        )
    if "CreateTableDefaultPermissions" in data:
        import aws_sdk_glue.types.principal_permissions_list

        out["create_table_default_permissions"] = (
            aws_sdk_glue.types.principal_permissions_list.deserialize_aws_json_1_1(
                data["CreateTableDefaultPermissions"]
            )
        )
    if "CreateDatabaseDefaultPermissions" in data:
        import aws_sdk_glue.types.principal_permissions_list

        out["create_database_default_permissions"] = (
            aws_sdk_glue.types.principal_permissions_list.deserialize_aws_json_1_1(
                data["CreateDatabaseDefaultPermissions"]
            )
        )
    if "AllowFullTableExternalDataAccess" in data:
        import aws_sdk_glue.types.allow_full_table_external_data_access_enum

        out["allow_full_table_external_data_access"] = (
            aws_sdk_glue.types.allow_full_table_external_data_access_enum.deserialize_aws_json_1_1(
                data["AllowFullTableExternalDataAccess"]
            )
        )
    return out

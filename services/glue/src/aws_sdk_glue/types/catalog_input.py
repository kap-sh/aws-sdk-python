"""Generated from Smithy shape ``com.amazonaws.glue#CatalogInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.allow_full_table_external_data_access_enum
    import aws_sdk_glue.types.catalog_properties
    import aws_sdk_glue.types.description_string
    import aws_sdk_glue.types.federated_catalog
    import aws_sdk_glue.types.overwrite_child_resource_permissions_with_default_enum
    import aws_sdk_glue.types.parameters_map
    import aws_sdk_glue.types.principal_permissions_list
    import aws_sdk_glue.types.target_redshift_catalog


class CatalogInput(TypedDict):
    description: NotRequired["aws_sdk_glue.types.description_string.DescriptionString"]
    """<p>Description string, not more than 2048 bytes long, matching the URI address multi-line string pattern. A description of the catalog.</p>"""
    federated_catalog: NotRequired[
        "aws_sdk_glue.types.federated_catalog.FederatedCatalog"
    ]
    """<p>A <code>FederatedCatalog</code> object. A <code>FederatedCatalog</code> structure that references an entity outside the Glue Data Catalog, for example a Redshift database.</p>"""
    parameters: NotRequired["aws_sdk_glue.types.parameters_map.ParametersMap"]
    """<p>A map array of key-value pairs that define the parameters and properties of the catalog.</p>"""
    target_redshift_catalog: NotRequired[
        "aws_sdk_glue.types.target_redshift_catalog.TargetRedshiftCatalog"
    ]
    """<p>A <code>TargetRedshiftCatalog</code> object that describes a target catalog for resource linking.</p>"""
    catalog_properties: NotRequired[
        "aws_sdk_glue.types.catalog_properties.CatalogProperties"
    ]
    """<p>A <code>CatalogProperties</code> object that specifies data lake access properties and other custom properties.</p>"""
    create_table_default_permissions: NotRequired[
        "aws_sdk_glue.types.principal_permissions_list.PrincipalPermissionsList"
    ]
    """<p>An array of <code>PrincipalPermissions</code> objects. Creates a set of default permissions on the table(s) for principals. Used by Amazon Web Services Lake Formation. Typically should be explicitly set as an empty list.</p>"""
    create_database_default_permissions: NotRequired[
        "aws_sdk_glue.types.principal_permissions_list.PrincipalPermissionsList"
    ]
    """<p>An array of <code>PrincipalPermissions</code> objects. Creates a set of default permissions on the database(s) for principals. Used by Amazon Web Services Lake Formation. Typically should be explicitly set as an empty list.</p>"""
    allow_full_table_external_data_access: NotRequired[
        "aws_sdk_glue.types.allow_full_table_external_data_access_enum.AllowFullTableExternalDataAccessEnum"
    ]
    """<p> Allows third-party engines to access data in Amazon S3 locations that are registered with Lake Formation. </p>"""
    overwrite_child_resource_permissions_with_default: NotRequired[
        "aws_sdk_glue.types.overwrite_child_resource_permissions_with_default_enum.OverwriteChildResourcePermissionsWithDefaultEnum"
    ]
    """<p> Overwrites existing Amazon Web Services Lake Formation permissions with <code>CatalogInput$CreateTableDefaultPermissions</code> and <code>CatalogInput$CreateDatabaseDefaultPermissions</code> for all child resources. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CatalogInput) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "federated_catalog" in value:
        import aws_sdk_glue.types.federated_catalog

        out["FederatedCatalog"] = (
            aws_sdk_glue.types.federated_catalog.serialize_aws_json_1_1(
                value["federated_catalog"]
            )
        )
    if "parameters" in value:
        import aws_sdk_glue.types.parameters_map

        out["Parameters"] = aws_sdk_glue.types.parameters_map.serialize_aws_json_1_1(
            value["parameters"]
        )
    if "target_redshift_catalog" in value:
        import aws_sdk_glue.types.target_redshift_catalog

        out["TargetRedshiftCatalog"] = (
            aws_sdk_glue.types.target_redshift_catalog.serialize_aws_json_1_1(
                value["target_redshift_catalog"]
            )
        )
    if "catalog_properties" in value:
        import aws_sdk_glue.types.catalog_properties

        out["CatalogProperties"] = (
            aws_sdk_glue.types.catalog_properties.serialize_aws_json_1_1(
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
    if "overwrite_child_resource_permissions_with_default" in value:
        import aws_sdk_glue.types.overwrite_child_resource_permissions_with_default_enum

        out["OverwriteChildResourcePermissionsWithDefault"] = (
            aws_sdk_glue.types.overwrite_child_resource_permissions_with_default_enum.serialize_aws_json_1_1(
                value["overwrite_child_resource_permissions_with_default"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CatalogInput:
    out: CatalogInput = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "FederatedCatalog" in data:
        import aws_sdk_glue.types.federated_catalog

        out["federated_catalog"] = (
            aws_sdk_glue.types.federated_catalog.deserialize_aws_json_1_1(
                data["FederatedCatalog"]
            )
        )
    if "Parameters" in data:
        import aws_sdk_glue.types.parameters_map

        out["parameters"] = aws_sdk_glue.types.parameters_map.deserialize_aws_json_1_1(
            data["Parameters"]
        )
    if "TargetRedshiftCatalog" in data:
        import aws_sdk_glue.types.target_redshift_catalog

        out["target_redshift_catalog"] = (
            aws_sdk_glue.types.target_redshift_catalog.deserialize_aws_json_1_1(
                data["TargetRedshiftCatalog"]
            )
        )
    if "CatalogProperties" in data:
        import aws_sdk_glue.types.catalog_properties

        out["catalog_properties"] = (
            aws_sdk_glue.types.catalog_properties.deserialize_aws_json_1_1(
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
    if "OverwriteChildResourcePermissionsWithDefault" in data:
        import aws_sdk_glue.types.overwrite_child_resource_permissions_with_default_enum

        out["overwrite_child_resource_permissions_with_default"] = (
            aws_sdk_glue.types.overwrite_child_resource_permissions_with_default_enum.deserialize_aws_json_1_1(
                data["OverwriteChildResourcePermissionsWithDefault"]
            )
        )
    return out

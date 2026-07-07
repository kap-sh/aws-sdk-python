"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#MigrationProject``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.data_provider_descriptor_list
    import aws_sdk_database_migration_service.types.iso8601_date_time
    import aws_sdk_database_migration_service.types.sc_application_attributes
    import aws_sdk_database_migration_service.types.string


class MigrationProject(TypedDict, closed=True):
    migration_project_name: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The name of the migration project.</p>"""
    migration_project_arn: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The ARN string that uniquely identifies the migration project.</p>"""
    migration_project_creation_time: NotRequired[
        "aws_sdk_database_migration_service.types.iso8601_date_time.Iso8601DateTime"
    ]
    """<p>The time when the migration project was created.</p>"""
    source_data_provider_descriptors: NotRequired[
        "aws_sdk_database_migration_service.types.data_provider_descriptor_list.DataProviderDescriptorList"
    ]
    """<p>Information about the source data provider, including the name or ARN, and Secrets Manager parameters.</p>"""
    target_data_provider_descriptors: NotRequired[
        "aws_sdk_database_migration_service.types.data_provider_descriptor_list.DataProviderDescriptorList"
    ]
    """<p>Information about the target data provider, including the name or ARN, and Secrets Manager parameters.</p>"""
    instance_profile_arn: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) of the instance profile for your migration project.</p>"""
    instance_profile_name: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The name of the associated instance profile.</p>"""
    transformation_rules: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The settings in JSON format for migration rules. Migration rules make it possible for you to change the object names according to the rules that you specify. For example, you can change an object name to lowercase or uppercase, add or remove a prefix or suffix, or rename objects.</p>"""
    description: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>A user-friendly description of the migration project.</p>"""
    schema_conversion_application_attributes: NotRequired[
        "aws_sdk_database_migration_service.types.sc_application_attributes.SCApplicationAttributes"
    ]
    """<p>The schema conversion application attributes, including the Amazon S3 bucket name and Amazon S3 role ARN.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MigrationProject) -> dict:
    out: dict = {}
    if "migration_project_name" in value:
        out["MigrationProjectName"] = value["migration_project_name"]
    if "migration_project_arn" in value:
        out["MigrationProjectArn"] = value["migration_project_arn"]
    if "migration_project_creation_time" in value:
        import aws_sdk_database_migration_service.types.iso8601_date_time

        out["MigrationProjectCreationTime"] = (
            aws_sdk_database_migration_service.types.iso8601_date_time.serialize_aws_json_1_1(
                value["migration_project_creation_time"]
            )
        )
    if "source_data_provider_descriptors" in value:
        import aws_sdk_database_migration_service.types.data_provider_descriptor_list

        out["SourceDataProviderDescriptors"] = (
            aws_sdk_database_migration_service.types.data_provider_descriptor_list.serialize_aws_json_1_1(
                value["source_data_provider_descriptors"]
            )
        )
    if "target_data_provider_descriptors" in value:
        import aws_sdk_database_migration_service.types.data_provider_descriptor_list

        out["TargetDataProviderDescriptors"] = (
            aws_sdk_database_migration_service.types.data_provider_descriptor_list.serialize_aws_json_1_1(
                value["target_data_provider_descriptors"]
            )
        )
    if "instance_profile_arn" in value:
        out["InstanceProfileArn"] = value["instance_profile_arn"]
    if "instance_profile_name" in value:
        out["InstanceProfileName"] = value["instance_profile_name"]
    if "transformation_rules" in value:
        out["TransformationRules"] = value["transformation_rules"]
    if "description" in value:
        out["Description"] = value["description"]
    if "schema_conversion_application_attributes" in value:
        import aws_sdk_database_migration_service.types.sc_application_attributes

        out["SchemaConversionApplicationAttributes"] = (
            aws_sdk_database_migration_service.types.sc_application_attributes.serialize_aws_json_1_1(
                value["schema_conversion_application_attributes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MigrationProject:
    out: MigrationProject = {}  # type: ignore[typeddict-item]
    if "MigrationProjectName" in data:
        out["migration_project_name"] = data["MigrationProjectName"]
    if "MigrationProjectArn" in data:
        out["migration_project_arn"] = data["MigrationProjectArn"]
    if "MigrationProjectCreationTime" in data:
        import aws_sdk_database_migration_service.types.iso8601_date_time

        out["migration_project_creation_time"] = (
            aws_sdk_database_migration_service.types.iso8601_date_time.deserialize_aws_json_1_1(
                data["MigrationProjectCreationTime"]
            )
        )
    if "SourceDataProviderDescriptors" in data:
        import aws_sdk_database_migration_service.types.data_provider_descriptor_list

        out["source_data_provider_descriptors"] = (
            aws_sdk_database_migration_service.types.data_provider_descriptor_list.deserialize_aws_json_1_1(
                data["SourceDataProviderDescriptors"]
            )
        )
    if "TargetDataProviderDescriptors" in data:
        import aws_sdk_database_migration_service.types.data_provider_descriptor_list

        out["target_data_provider_descriptors"] = (
            aws_sdk_database_migration_service.types.data_provider_descriptor_list.deserialize_aws_json_1_1(
                data["TargetDataProviderDescriptors"]
            )
        )
    if "InstanceProfileArn" in data:
        out["instance_profile_arn"] = data["InstanceProfileArn"]
    if "InstanceProfileName" in data:
        out["instance_profile_name"] = data["InstanceProfileName"]
    if "TransformationRules" in data:
        out["transformation_rules"] = data["TransformationRules"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "SchemaConversionApplicationAttributes" in data:
        import aws_sdk_database_migration_service.types.sc_application_attributes

        out["schema_conversion_application_attributes"] = (
            aws_sdk_database_migration_service.types.sc_application_attributes.deserialize_aws_json_1_1(
                data["SchemaConversionApplicationAttributes"]
            )
        )
    return out

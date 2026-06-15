"""Generated from Smithy shape ``com.amazonaws.lightsail#RelationalDatabase``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.boolean
    import aws_sdk_lightsail.types.iso_date
    import aws_sdk_lightsail.types.non_empty_string
    import aws_sdk_lightsail.types.pending_maintenance_action_list
    import aws_sdk_lightsail.types.pending_modified_relational_database_values
    import aws_sdk_lightsail.types.relational_database_endpoint
    import aws_sdk_lightsail.types.relational_database_hardware
    import aws_sdk_lightsail.types.resource_location
    import aws_sdk_lightsail.types.resource_name
    import aws_sdk_lightsail.types.resource_type
    import aws_sdk_lightsail.types.string
    import aws_sdk_lightsail.types.tag_list


class RelationalDatabase(TypedDict):
    name: NotRequired["aws_sdk_lightsail.types.resource_name.ResourceName"]
    """<p>The unique name of the database resource in Lightsail.</p>"""
    arn: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the database.</p>"""
    support_code: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The support code for the database. Include this code in your email to support when you have questions about a database in Lightsail. This code enables our support team to look up your Lightsail information more easily.</p>"""
    created_at: NotRequired["aws_sdk_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp when the database was created. Formatted in Unix time.</p>"""
    location: NotRequired["aws_sdk_lightsail.types.resource_location.ResourceLocation"]
    """<p>The Region name and Availability Zone where the database is located.</p>"""
    resource_type: NotRequired["aws_sdk_lightsail.types.resource_type.ResourceType"]
    """<p>The Lightsail resource type for the database (for example, <code>RelationalDatabase</code>).</p>"""
    tags: NotRequired["aws_sdk_lightsail.types.tag_list.TagList"]
    r"""<p>The tag keys and optional values for the resource. For more information about tags in Lightsail, see the <a href=\"https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags\">Amazon Lightsail Developer Guide</a>.</p>"""
    relational_database_blueprint_id: NotRequired[
        "aws_sdk_lightsail.types.non_empty_string.NonEmptyString"
    ]
    """<p>The blueprint ID for the database. A blueprint describes the major engine version of a database.</p>"""
    relational_database_bundle_id: NotRequired[
        "aws_sdk_lightsail.types.non_empty_string.NonEmptyString"
    ]
    """<p>The bundle ID for the database. A bundle describes the performance specifications for your database.</p>"""
    master_database_name: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The name of the master database created when the Lightsail database resource is created.</p>"""
    hardware: NotRequired[
        "aws_sdk_lightsail.types.relational_database_hardware.RelationalDatabaseHardware"
    ]
    """<p>Describes the hardware of the database.</p>"""
    state: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>Describes the current state of the database.</p>"""
    secondary_availability_zone: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>Describes the secondary Availability Zone of a high availability database.</p> <p>The secondary database is used for failover support of a high availability database.</p>"""
    backup_retention_enabled: NotRequired["aws_sdk_lightsail.types.boolean.boolean"]
    """<p>A Boolean value indicating whether automated backup retention is enabled for the database.</p>"""
    pending_modified_values: NotRequired[
        "aws_sdk_lightsail.types.pending_modified_relational_database_values.PendingModifiedRelationalDatabaseValues"
    ]
    """<p>Describes pending database value modifications.</p>"""
    engine: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The database software (for example, <code>MySQL</code>).</p>"""
    engine_version: NotRequired[
        "aws_sdk_lightsail.types.non_empty_string.NonEmptyString"
    ]
    """<p>The database engine version (for example, <code>5.7.23</code>).</p>"""
    latest_restorable_time: NotRequired["aws_sdk_lightsail.types.iso_date.IsoDate"]
    """<p>The latest point in time to which the database can be restored. Formatted in Unix time.</p>"""
    master_username: NotRequired[
        "aws_sdk_lightsail.types.non_empty_string.NonEmptyString"
    ]
    """<p>The master user name of the database.</p>"""
    parameter_apply_status: NotRequired[
        "aws_sdk_lightsail.types.non_empty_string.NonEmptyString"
    ]
    """<p>The status of parameter updates for the database.</p>"""
    preferred_backup_window: NotRequired[
        "aws_sdk_lightsail.types.non_empty_string.NonEmptyString"
    ]
    """<p>The daily time range during which automated backups are created for the database (for example, <code>16:00-16:30</code>).</p>"""
    preferred_maintenance_window: NotRequired[
        "aws_sdk_lightsail.types.non_empty_string.NonEmptyString"
    ]
    """<p>The weekly time range during which system maintenance can occur on the database.</p> <p>In the format <code>ddd:hh24:mi-ddd:hh24:mi</code>. For example, <code>Tue:17:00-Tue:17:30</code>.</p>"""
    publicly_accessible: NotRequired["aws_sdk_lightsail.types.boolean.boolean"]
    """<p>A Boolean value indicating whether the database is publicly accessible.</p>"""
    master_endpoint: NotRequired[
        "aws_sdk_lightsail.types.relational_database_endpoint.RelationalDatabaseEndpoint"
    ]
    """<p>The master endpoint for the database.</p>"""
    pending_maintenance_actions: NotRequired[
        "aws_sdk_lightsail.types.pending_maintenance_action_list.PendingMaintenanceActionList"
    ]
    """<p>Describes the pending maintenance actions for the database.</p>"""
    ca_certificate_identifier: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The certificate associated with the database.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelationalDatabase) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "support_code" in value:
        out["supportCode"] = value["support_code"]
    if "created_at" in value:
        import aws_sdk_lightsail.types.iso_date

        out["createdAt"] = aws_sdk_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "location" in value:
        import aws_sdk_lightsail.types.resource_location

        out["location"] = (
            aws_sdk_lightsail.types.resource_location.serialize_aws_json_1_1(
                value["location"]
            )
        )
    if "resource_type" in value:
        import aws_sdk_lightsail.types.resource_type

        out["resourceType"] = (
            aws_sdk_lightsail.types.resource_type.serialize_aws_json_1_1(
                value["resource_type"]
            )
        )
    if "tags" in value:
        import aws_sdk_lightsail.types.tag_list

        out["tags"] = aws_sdk_lightsail.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "relational_database_blueprint_id" in value:
        out["relationalDatabaseBlueprintId"] = value["relational_database_blueprint_id"]
    if "relational_database_bundle_id" in value:
        out["relationalDatabaseBundleId"] = value["relational_database_bundle_id"]
    if "master_database_name" in value:
        out["masterDatabaseName"] = value["master_database_name"]
    if "hardware" in value:
        import aws_sdk_lightsail.types.relational_database_hardware

        out["hardware"] = (
            aws_sdk_lightsail.types.relational_database_hardware.serialize_aws_json_1_1(
                value["hardware"]
            )
        )
    if "state" in value:
        out["state"] = value["state"]
    if "secondary_availability_zone" in value:
        out["secondaryAvailabilityZone"] = value["secondary_availability_zone"]
    if "backup_retention_enabled" in value:
        out["backupRetentionEnabled"] = value["backup_retention_enabled"]
    if "pending_modified_values" in value:
        import aws_sdk_lightsail.types.pending_modified_relational_database_values

        out["pendingModifiedValues"] = (
            aws_sdk_lightsail.types.pending_modified_relational_database_values.serialize_aws_json_1_1(
                value["pending_modified_values"]
            )
        )
    if "engine" in value:
        out["engine"] = value["engine"]
    if "engine_version" in value:
        out["engineVersion"] = value["engine_version"]
    if "latest_restorable_time" in value:
        import aws_sdk_lightsail.types.iso_date

        out["latestRestorableTime"] = (
            aws_sdk_lightsail.types.iso_date.serialize_aws_json_1_1(
                value["latest_restorable_time"]
            )
        )
    if "master_username" in value:
        out["masterUsername"] = value["master_username"]
    if "parameter_apply_status" in value:
        out["parameterApplyStatus"] = value["parameter_apply_status"]
    if "preferred_backup_window" in value:
        out["preferredBackupWindow"] = value["preferred_backup_window"]
    if "preferred_maintenance_window" in value:
        out["preferredMaintenanceWindow"] = value["preferred_maintenance_window"]
    if "publicly_accessible" in value:
        out["publiclyAccessible"] = value["publicly_accessible"]
    if "master_endpoint" in value:
        import aws_sdk_lightsail.types.relational_database_endpoint

        out["masterEndpoint"] = (
            aws_sdk_lightsail.types.relational_database_endpoint.serialize_aws_json_1_1(
                value["master_endpoint"]
            )
        )
    if "pending_maintenance_actions" in value:
        import aws_sdk_lightsail.types.pending_maintenance_action_list

        out["pendingMaintenanceActions"] = (
            aws_sdk_lightsail.types.pending_maintenance_action_list.serialize_aws_json_1_1(
                value["pending_maintenance_actions"]
            )
        )
    if "ca_certificate_identifier" in value:
        out["caCertificateIdentifier"] = value["ca_certificate_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RelationalDatabase:
    out: RelationalDatabase = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "supportCode" in data:
        out["support_code"] = data["supportCode"]
    if "createdAt" in data:
        import aws_sdk_lightsail.types.iso_date

        out["created_at"] = aws_sdk_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if "location" in data:
        import aws_sdk_lightsail.types.resource_location

        out["location"] = (
            aws_sdk_lightsail.types.resource_location.deserialize_aws_json_1_1(
                data["location"]
            )
        )
    if "resourceType" in data:
        import aws_sdk_lightsail.types.resource_type

        out["resource_type"] = (
            aws_sdk_lightsail.types.resource_type.deserialize_aws_json_1_1(
                data["resourceType"]
            )
        )
    if "tags" in data:
        import aws_sdk_lightsail.types.tag_list

        out["tags"] = aws_sdk_lightsail.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if "relationalDatabaseBlueprintId" in data:
        out["relational_database_blueprint_id"] = data["relationalDatabaseBlueprintId"]
    if "relationalDatabaseBundleId" in data:
        out["relational_database_bundle_id"] = data["relationalDatabaseBundleId"]
    if "masterDatabaseName" in data:
        out["master_database_name"] = data["masterDatabaseName"]
    if "hardware" in data:
        import aws_sdk_lightsail.types.relational_database_hardware

        out["hardware"] = (
            aws_sdk_lightsail.types.relational_database_hardware.deserialize_aws_json_1_1(
                data["hardware"]
            )
        )
    if "state" in data:
        out["state"] = data["state"]
    if "secondaryAvailabilityZone" in data:
        out["secondary_availability_zone"] = data["secondaryAvailabilityZone"]
    if "backupRetentionEnabled" in data:
        out["backup_retention_enabled"] = data["backupRetentionEnabled"]
    if "pendingModifiedValues" in data:
        import aws_sdk_lightsail.types.pending_modified_relational_database_values

        out["pending_modified_values"] = (
            aws_sdk_lightsail.types.pending_modified_relational_database_values.deserialize_aws_json_1_1(
                data["pendingModifiedValues"]
            )
        )
    if "engine" in data:
        out["engine"] = data["engine"]
    if "engineVersion" in data:
        out["engine_version"] = data["engineVersion"]
    if "latestRestorableTime" in data:
        import aws_sdk_lightsail.types.iso_date

        out["latest_restorable_time"] = (
            aws_sdk_lightsail.types.iso_date.deserialize_aws_json_1_1(
                data["latestRestorableTime"]
            )
        )
    if "masterUsername" in data:
        out["master_username"] = data["masterUsername"]
    if "parameterApplyStatus" in data:
        out["parameter_apply_status"] = data["parameterApplyStatus"]
    if "preferredBackupWindow" in data:
        out["preferred_backup_window"] = data["preferredBackupWindow"]
    if "preferredMaintenanceWindow" in data:
        out["preferred_maintenance_window"] = data["preferredMaintenanceWindow"]
    if "publiclyAccessible" in data:
        out["publicly_accessible"] = data["publiclyAccessible"]
    if "masterEndpoint" in data:
        import aws_sdk_lightsail.types.relational_database_endpoint

        out["master_endpoint"] = (
            aws_sdk_lightsail.types.relational_database_endpoint.deserialize_aws_json_1_1(
                data["masterEndpoint"]
            )
        )
    if "pendingMaintenanceActions" in data:
        import aws_sdk_lightsail.types.pending_maintenance_action_list

        out["pending_maintenance_actions"] = (
            aws_sdk_lightsail.types.pending_maintenance_action_list.deserialize_aws_json_1_1(
                data["pendingMaintenanceActions"]
            )
        )
    if "caCertificateIdentifier" in data:
        out["ca_certificate_identifier"] = data["caCertificateIdentifier"]
    return out

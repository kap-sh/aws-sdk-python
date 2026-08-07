"""Generated from Smithy shape ``com.amazonaws.docdb#PendingModifiedValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.boolean_optional
    import capo_docdb.types.integer_optional
    import capo_docdb.types.pending_cloudwatch_logs_exports
    import capo_docdb.types.string


class PendingModifiedValues(TypedDict, closed=True):
    db_instance_class: NotRequired["capo_docdb.types.string.String"]
    """<p> Contains the new <code>DBInstanceClass</code> for the instance that will be applied or is currently being applied. </p>"""
    allocated_storage: NotRequired["capo_docdb.types.integer_optional.IntegerOptional"]
    """<p> Contains the new <code>AllocatedStorage</code> size for then instance that will be applied or is currently being applied. </p>"""
    master_user_password: NotRequired["capo_docdb.types.string.String"]
    """<p>Contains the pending or currently in-progress change of the master credentials for the instance.</p>"""
    port: NotRequired["capo_docdb.types.integer_optional.IntegerOptional"]
    """<p>Specifies the pending port for the instance.</p>"""
    backup_retention_period: NotRequired[
        "capo_docdb.types.integer_optional.IntegerOptional"
    ]
    """<p>Specifies the pending number of days for which automated backups are retained.</p>"""
    multi_az: NotRequired["capo_docdb.types.boolean_optional.BooleanOptional"]
    """<p>Indicates that the Single-AZ instance is to change to a Multi-AZ deployment.</p>"""
    engine_version: NotRequired["capo_docdb.types.string.String"]
    """<p>Indicates the database engine version.</p>"""
    license_model: NotRequired["capo_docdb.types.string.String"]
    """<p>The license model for the instance.</p> <p>Valid values: <code>license-included</code>, <code>bring-your-own-license</code>, <code>general-public-license</code> </p>"""
    iops: NotRequired["capo_docdb.types.integer_optional.IntegerOptional"]
    """<p>Specifies the new Provisioned IOPS value for the instance that will be applied or is currently being applied.</p>"""
    db_instance_identifier: NotRequired["capo_docdb.types.string.String"]
    """<p> Contains the new <code>DBInstanceIdentifier</code> for the instance that will be applied or is currently being applied. </p>"""
    storage_type: NotRequired["capo_docdb.types.string.String"]
    """<p>Specifies the storage type to be associated with the instance.</p>"""
    ca_certificate_identifier: NotRequired["capo_docdb.types.string.String"]
    """<p>Specifies the identifier of the certificate authority (CA) certificate for the DB instance.</p>"""
    db_subnet_group_name: NotRequired["capo_docdb.types.string.String"]
    """<p>The new subnet group for the instance. </p>"""
    pending_cloudwatch_logs_exports: NotRequired[
        "capo_docdb.types.pending_cloudwatch_logs_exports.PendingCloudwatchLogsExports"
    ]
    """<p>A list of the log types whose configuration is still pending. These log types are in the process of being activated or deactivated.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PendingModifiedValues, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_instance_class" in value:
        pairs.append((f"{key_prefix}DBInstanceClass", str(value["db_instance_class"])))
    if "allocated_storage" in value:
        pairs.append((f"{key_prefix}AllocatedStorage", str(value["allocated_storage"])))
    if "master_user_password" in value:
        pairs.append(
            (f"{key_prefix}MasterUserPassword", str(value["master_user_password"]))
        )
    if "port" in value:
        pairs.append((f"{key_prefix}Port", str(value["port"])))
    if "backup_retention_period" in value:
        pairs.append(
            (
                f"{key_prefix}BackupRetentionPeriod",
                str(value["backup_retention_period"]),
            )
        )
    if "multi_az" in value:
        pairs.append((f"{key_prefix}MultiAZ", "true" if value["multi_az"] else "false"))
    if "engine_version" in value:
        pairs.append((f"{key_prefix}EngineVersion", str(value["engine_version"])))
    if "license_model" in value:
        pairs.append((f"{key_prefix}LicenseModel", str(value["license_model"])))
    if "iops" in value:
        pairs.append((f"{key_prefix}Iops", str(value["iops"])))
    if "db_instance_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBInstanceIdentifier", str(value["db_instance_identifier"]))
        )
    if "storage_type" in value:
        pairs.append((f"{key_prefix}StorageType", str(value["storage_type"])))
    if "ca_certificate_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}CACertificateIdentifier",
                str(value["ca_certificate_identifier"]),
            )
        )
    if "db_subnet_group_name" in value:
        pairs.append(
            (f"{key_prefix}DBSubnetGroupName", str(value["db_subnet_group_name"]))
        )
    if "pending_cloudwatch_logs_exports" in value:
        import capo_docdb.types.pending_cloudwatch_logs_exports

        capo_docdb.types.pending_cloudwatch_logs_exports.serialize_query(
            value["pending_cloudwatch_logs_exports"],
            pairs,
            f"{key_prefix}PendingCloudwatchLogsExports",
        )


def deserialize_query(el: Element) -> PendingModifiedValues:
    out: PendingModifiedValues = {}  # type: ignore[typeddict-item]
    child_db_instance_class = el.find("DBInstanceClass")
    if child_db_instance_class is not None:
        out["db_instance_class"] = str(child_db_instance_class.text or "")
    child_allocated_storage = el.find("AllocatedStorage")
    if child_allocated_storage is not None:
        out["allocated_storage"] = int(child_allocated_storage.text or "")
    child_master_user_password = el.find("MasterUserPassword")
    if child_master_user_password is not None:
        out["master_user_password"] = str(child_master_user_password.text or "")
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    child_backup_retention_period = el.find("BackupRetentionPeriod")
    if child_backup_retention_period is not None:
        out["backup_retention_period"] = int(child_backup_retention_period.text or "")
    child_multi_az = el.find("MultiAZ")
    if child_multi_az is not None:
        out["multi_az"] = (child_multi_az.text or "").lower() == "true"
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_license_model = el.find("LicenseModel")
    if child_license_model is not None:
        out["license_model"] = str(child_license_model.text or "")
    child_iops = el.find("Iops")
    if child_iops is not None:
        out["iops"] = int(child_iops.text or "")
    child_db_instance_identifier = el.find("DBInstanceIdentifier")
    if child_db_instance_identifier is not None:
        out["db_instance_identifier"] = str(child_db_instance_identifier.text or "")
    child_storage_type = el.find("StorageType")
    if child_storage_type is not None:
        out["storage_type"] = str(child_storage_type.text or "")
    child_ca_certificate_identifier = el.find("CACertificateIdentifier")
    if child_ca_certificate_identifier is not None:
        out["ca_certificate_identifier"] = str(
            child_ca_certificate_identifier.text or ""
        )
    child_db_subnet_group_name = el.find("DBSubnetGroupName")
    if child_db_subnet_group_name is not None:
        out["db_subnet_group_name"] = str(child_db_subnet_group_name.text or "")
    child_pending_cloudwatch_logs_exports = el.find("PendingCloudwatchLogsExports")
    if child_pending_cloudwatch_logs_exports is not None:
        import capo_docdb.types.pending_cloudwatch_logs_exports

        out["pending_cloudwatch_logs_exports"] = (
            capo_docdb.types.pending_cloudwatch_logs_exports.deserialize_query(
                child_pending_cloudwatch_logs_exports
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.neptune#DBEngineVersion``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.boolean
    import aws_sdk_neptune.types.character_set
    import aws_sdk_neptune.types.log_type_list
    import aws_sdk_neptune.types.string
    import aws_sdk_neptune.types.supported_character_sets_list
    import aws_sdk_neptune.types.supported_timezones_list
    import aws_sdk_neptune.types.valid_upgrade_target_list


class DBEngineVersion(TypedDict):
    engine: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>The name of the database engine.</p>"""
    engine_version: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>The version number of the database engine.</p>"""
    db_parameter_group_family: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>The name of the DB parameter group family for the database engine.</p>"""
    db_engine_description: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>The description of the database engine.</p>"""
    db_engine_version_description: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>The description of the database engine version.</p>"""
    default_character_set: NotRequired[
        "aws_sdk_neptune.types.character_set.CharacterSet"
    ]
    """<p> <i>(Not supported by Neptune)</i> </p>"""
    supported_character_sets: NotRequired[
        "aws_sdk_neptune.types.supported_character_sets_list.SupportedCharacterSetsList"
    ]
    """<p> <i>(Not supported by Neptune)</i> </p>"""
    valid_upgrade_target: NotRequired[
        "aws_sdk_neptune.types.valid_upgrade_target_list.ValidUpgradeTargetList"
    ]
    """<p>A list of engine versions that this database engine version can be upgraded to.</p>"""
    supported_timezones: NotRequired[
        "aws_sdk_neptune.types.supported_timezones_list.SupportedTimezonesList"
    ]
    """<p>A list of the time zones supported by this engine for the <code>Timezone</code> parameter of the <code>CreateDBInstance</code> action.</p>"""
    exportable_log_types: NotRequired["aws_sdk_neptune.types.log_type_list.LogTypeList"]
    """<p>The types of logs that the database engine has available for export to CloudWatch Logs.</p>"""
    supports_log_exports_to_cloudwatch_logs: NotRequired[
        "aws_sdk_neptune.types.boolean.Boolean"
    ]
    """<p>A value that indicates whether the engine version supports exporting the log types specified by ExportableLogTypes to CloudWatch Logs.</p>"""
    supports_read_replica: NotRequired["aws_sdk_neptune.types.boolean.Boolean"]
    """<p>Indicates whether the database engine version supports read replicas.</p>"""
    supports_global_databases: NotRequired["aws_sdk_neptune.types.boolean.Boolean"]
    """<p>A value that indicates whether you can use Aurora global databases with a specific DB engine version.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBEngineVersion, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "engine" in value:
        pairs.append((f"{prefix}.Engine", str(value["engine"])))
    if "engine_version" in value:
        pairs.append((f"{prefix}.EngineVersion", str(value["engine_version"])))
    if "db_parameter_group_family" in value:
        pairs.append(
            (
                f"{prefix}.DBParameterGroupFamily",
                str(value["db_parameter_group_family"]),
            )
        )
    if "db_engine_description" in value:
        pairs.append(
            (f"{prefix}.DBEngineDescription", str(value["db_engine_description"]))
        )
    if "db_engine_version_description" in value:
        pairs.append(
            (
                f"{prefix}.DBEngineVersionDescription",
                str(value["db_engine_version_description"]),
            )
        )
    if "default_character_set" in value:
        import aws_sdk_neptune.types.character_set

        aws_sdk_neptune.types.character_set.serialize_query(
            value["default_character_set"], pairs, f"{prefix}.DefaultCharacterSet"
        )
    if "supported_character_sets" in value:
        import aws_sdk_neptune.types.supported_character_sets_list

        aws_sdk_neptune.types.supported_character_sets_list.serialize_query(
            value["supported_character_sets"], pairs, f"{prefix}.SupportedCharacterSets"
        )
    if "valid_upgrade_target" in value:
        import aws_sdk_neptune.types.valid_upgrade_target_list

        aws_sdk_neptune.types.valid_upgrade_target_list.serialize_query(
            value["valid_upgrade_target"], pairs, f"{prefix}.ValidUpgradeTarget"
        )
    if "supported_timezones" in value:
        import aws_sdk_neptune.types.supported_timezones_list

        aws_sdk_neptune.types.supported_timezones_list.serialize_query(
            value["supported_timezones"], pairs, f"{prefix}.SupportedTimezones"
        )
    if "exportable_log_types" in value:
        import aws_sdk_neptune.types.log_type_list

        aws_sdk_neptune.types.log_type_list.serialize_query(
            value["exportable_log_types"], pairs, f"{prefix}.ExportableLogTypes"
        )
    if "supports_log_exports_to_cloudwatch_logs" in value:
        pairs.append(
            (
                f"{prefix}.SupportsLogExportsToCloudwatchLogs",
                "true" if value["supports_log_exports_to_cloudwatch_logs"] else "false",
            )
        )
    if "supports_read_replica" in value:
        pairs.append(
            (
                f"{prefix}.SupportsReadReplica",
                "true" if value["supports_read_replica"] else "false",
            )
        )
    if "supports_global_databases" in value:
        pairs.append(
            (
                f"{prefix}.SupportsGlobalDatabases",
                "true" if value["supports_global_databases"] else "false",
            )
        )


def deserialize_query(el: Element) -> DBEngineVersion:
    out: DBEngineVersion = {}  # type: ignore[typeddict-item]
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_db_parameter_group_family = el.find("DBParameterGroupFamily")
    if child_db_parameter_group_family is not None:
        out["db_parameter_group_family"] = str(
            child_db_parameter_group_family.text or ""
        )
    child_db_engine_description = el.find("DBEngineDescription")
    if child_db_engine_description is not None:
        out["db_engine_description"] = str(child_db_engine_description.text or "")
    child_db_engine_version_description = el.find("DBEngineVersionDescription")
    if child_db_engine_version_description is not None:
        out["db_engine_version_description"] = str(
            child_db_engine_version_description.text or ""
        )
    child_default_character_set = el.find("DefaultCharacterSet")
    if child_default_character_set is not None:
        import aws_sdk_neptune.types.character_set

        out["default_character_set"] = (
            aws_sdk_neptune.types.character_set.deserialize_query(
                child_default_character_set
            )
        )
    child_supported_character_sets = el.find("SupportedCharacterSets")
    if child_supported_character_sets is not None:
        import aws_sdk_neptune.types.supported_character_sets_list

        out["supported_character_sets"] = (
            aws_sdk_neptune.types.supported_character_sets_list.deserialize_query(
                child_supported_character_sets
            )
        )
    child_valid_upgrade_target = el.find("ValidUpgradeTarget")
    if child_valid_upgrade_target is not None:
        import aws_sdk_neptune.types.valid_upgrade_target_list

        out["valid_upgrade_target"] = (
            aws_sdk_neptune.types.valid_upgrade_target_list.deserialize_query(
                child_valid_upgrade_target
            )
        )
    child_supported_timezones = el.find("SupportedTimezones")
    if child_supported_timezones is not None:
        import aws_sdk_neptune.types.supported_timezones_list

        out["supported_timezones"] = (
            aws_sdk_neptune.types.supported_timezones_list.deserialize_query(
                child_supported_timezones
            )
        )
    child_exportable_log_types = el.find("ExportableLogTypes")
    if child_exportable_log_types is not None:
        import aws_sdk_neptune.types.log_type_list

        out["exportable_log_types"] = (
            aws_sdk_neptune.types.log_type_list.deserialize_query(
                child_exportable_log_types
            )
        )
    child_supports_log_exports_to_cloudwatch_logs = el.find(
        "SupportsLogExportsToCloudwatchLogs"
    )
    if child_supports_log_exports_to_cloudwatch_logs is not None:
        out["supports_log_exports_to_cloudwatch_logs"] = (
            child_supports_log_exports_to_cloudwatch_logs.text or ""
        ).lower() == "true"
    child_supports_read_replica = el.find("SupportsReadReplica")
    if child_supports_read_replica is not None:
        out["supports_read_replica"] = (
            child_supports_read_replica.text or ""
        ).lower() == "true"
    child_supports_global_databases = el.find("SupportsGlobalDatabases")
    if child_supports_global_databases is not None:
        out["supports_global_databases"] = (
            child_supports_global_databases.text or ""
        ).lower() == "true"
    return out

"""Generated from Smithy shape ``com.amazonaws.rds#UpgradeTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean
    import capo_rds.types.boolean_optional
    import capo_rds.types.engine_mode_list
    import capo_rds.types.string


class UpgradeTarget(TypedDict, closed=True):
    engine: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the upgrade target database engine.</p>"""
    engine_version: NotRequired["capo_rds.types.string.String"]
    """<p>The version number of the upgrade target database engine.</p>"""
    description: NotRequired["capo_rds.types.string.String"]
    """<p>The version of the database engine that a DB instance can be upgraded to.</p>"""
    auto_upgrade: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether the target version is applied to any source DB instances that have <code>AutoMinorVersionUpgrade</code> set to true.</p> <p>This parameter is dynamic, and is set by RDS.</p>"""
    is_major_version_upgrade: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether upgrading to the target version requires upgrading the major version of the database engine.</p>"""
    supported_engine_modes: NotRequired[
        "capo_rds.types.engine_mode_list.EngineModeList"
    ]
    """<p>A list of the supported DB engine modes for the target engine version.</p>"""
    supports_parallel_query: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether you can use Aurora parallel query with the target engine version.</p>"""
    supports_global_databases: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether you can use Aurora global databases with the target engine version.</p>"""
    supports_babelfish: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Indicates whether you can use Babelfish for Aurora PostgreSQL with the target engine version.</p>"""
    supports_limitless_database: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether the DB engine version supports Aurora Limitless Database.</p>"""
    supports_local_write_forwarding: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether the target engine version supports forwarding write operations from reader DB instances to the writer DB instance in the DB cluster. By default, write operations aren't allowed on reader DB instances.</p> <p>Valid for: Aurora DB clusters only</p>"""
    supports_integrations: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether the DB engine version supports zero-ETL integrations with Amazon Redshift.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpgradeTarget, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "engine" in value:
        pairs.append((f"{prefix}.Engine", str(value["engine"])))
    if "engine_version" in value:
        pairs.append((f"{prefix}.EngineVersion", str(value["engine_version"])))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "auto_upgrade" in value:
        pairs.append(
            (f"{prefix}.AutoUpgrade", "true" if value["auto_upgrade"] else "false")
        )
    if "is_major_version_upgrade" in value:
        pairs.append(
            (
                f"{prefix}.IsMajorVersionUpgrade",
                "true" if value["is_major_version_upgrade"] else "false",
            )
        )
    if "supported_engine_modes" in value:
        import capo_rds.types.engine_mode_list

        capo_rds.types.engine_mode_list.serialize_query(
            value["supported_engine_modes"], pairs, f"{prefix}.SupportedEngineModes"
        )
    if "supports_parallel_query" in value:
        pairs.append(
            (
                f"{prefix}.SupportsParallelQuery",
                "true" if value["supports_parallel_query"] else "false",
            )
        )
    if "supports_global_databases" in value:
        pairs.append(
            (
                f"{prefix}.SupportsGlobalDatabases",
                "true" if value["supports_global_databases"] else "false",
            )
        )
    if "supports_babelfish" in value:
        pairs.append(
            (
                f"{prefix}.SupportsBabelfish",
                "true" if value["supports_babelfish"] else "false",
            )
        )
    if "supports_limitless_database" in value:
        pairs.append(
            (
                f"{prefix}.SupportsLimitlessDatabase",
                "true" if value["supports_limitless_database"] else "false",
            )
        )
    if "supports_local_write_forwarding" in value:
        pairs.append(
            (
                f"{prefix}.SupportsLocalWriteForwarding",
                "true" if value["supports_local_write_forwarding"] else "false",
            )
        )
    if "supports_integrations" in value:
        pairs.append(
            (
                f"{prefix}.SupportsIntegrations",
                "true" if value["supports_integrations"] else "false",
            )
        )


def deserialize_query(el: Element) -> UpgradeTarget:
    out: UpgradeTarget = {}  # type: ignore[typeddict-item]
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_auto_upgrade = el.find("AutoUpgrade")
    if child_auto_upgrade is not None:
        out["auto_upgrade"] = (child_auto_upgrade.text or "").lower() == "true"
    child_is_major_version_upgrade = el.find("IsMajorVersionUpgrade")
    if child_is_major_version_upgrade is not None:
        out["is_major_version_upgrade"] = (
            child_is_major_version_upgrade.text or ""
        ).lower() == "true"
    child_supported_engine_modes = el.find("SupportedEngineModes")
    if child_supported_engine_modes is not None:
        import capo_rds.types.engine_mode_list

        out["supported_engine_modes"] = (
            capo_rds.types.engine_mode_list.deserialize_query(
                child_supported_engine_modes
            )
        )
    child_supports_parallel_query = el.find("SupportsParallelQuery")
    if child_supports_parallel_query is not None:
        out["supports_parallel_query"] = (
            child_supports_parallel_query.text or ""
        ).lower() == "true"
    child_supports_global_databases = el.find("SupportsGlobalDatabases")
    if child_supports_global_databases is not None:
        out["supports_global_databases"] = (
            child_supports_global_databases.text or ""
        ).lower() == "true"
    child_supports_babelfish = el.find("SupportsBabelfish")
    if child_supports_babelfish is not None:
        out["supports_babelfish"] = (
            child_supports_babelfish.text or ""
        ).lower() == "true"
    child_supports_limitless_database = el.find("SupportsLimitlessDatabase")
    if child_supports_limitless_database is not None:
        out["supports_limitless_database"] = (
            child_supports_limitless_database.text or ""
        ).lower() == "true"
    child_supports_local_write_forwarding = el.find("SupportsLocalWriteForwarding")
    if child_supports_local_write_forwarding is not None:
        out["supports_local_write_forwarding"] = (
            child_supports_local_write_forwarding.text or ""
        ).lower() == "true"
    child_supports_integrations = el.find("SupportsIntegrations")
    if child_supports_integrations is not None:
        out["supports_integrations"] = (
            child_supports_integrations.text or ""
        ).lower() == "true"
    return out

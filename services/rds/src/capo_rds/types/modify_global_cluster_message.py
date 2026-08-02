"""Generated from Smithy shape ``com.amazonaws.rds#ModifyGlobalClusterMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean_optional
    import capo_rds.types.global_cluster_identifier
    import capo_rds.types.string


class ModifyGlobalClusterMessage(TypedDict, closed=True):
    global_cluster_identifier: NotRequired[
        "capo_rds.types.global_cluster_identifier.GlobalClusterIdentifier"
    ]
    """<p>The cluster identifier for the global cluster to modify. This parameter isn't case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing global database cluster.</p> </li> </ul>"""
    new_global_cluster_identifier: NotRequired[
        "capo_rds.types.global_cluster_identifier.GlobalClusterIdentifier"
    ]
    """<p>The new cluster identifier for the global database cluster. This value is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens.</p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>Can't end with a hyphen or contain two consecutive hyphens.</p> </li> </ul> <p>Example: <code>my-cluster2</code> </p>"""
    deletion_protection: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether to enable deletion protection for the global database cluster. The global database cluster can't be deleted when deletion protection is enabled.</p>"""
    engine_version: NotRequired["capo_rds.types.string.String"]
    """<p>The version number of the database engine to which you want to upgrade. </p> <p>To list all of the available engine versions for <code>aurora-mysql</code> (for MySQL-based Aurora global databases), use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine aurora-mysql --query '*[]|[?SupportsGlobalDatabases == `true`].[EngineVersion]'</code> </p> <p>To list all of the available engine versions for <code>aurora-postgresql</code> (for PostgreSQL-based Aurora global databases), use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine aurora-postgresql --query '*[]|[?SupportsGlobalDatabases == `true`].[EngineVersion]'</code> </p>"""
    allow_major_version_upgrade: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to allow major version upgrades.</p> <p>Constraints: Must be enabled if you specify a value for the <code>EngineVersion</code> parameter that's a different major version than the global cluster's current version.</p> <p>If you upgrade the major version of a global database, the cluster and DB instance parameter groups are set to the default parameter groups for the new version. Apply any custom parameter groups after completing the upgrade.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyGlobalClusterMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "global_cluster_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}GlobalClusterIdentifier",
                str(value["global_cluster_identifier"]),
            )
        )
    if "new_global_cluster_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}NewGlobalClusterIdentifier",
                str(value["new_global_cluster_identifier"]),
            )
        )
    if "deletion_protection" in value:
        pairs.append(
            (
                f"{key_prefix}DeletionProtection",
                "true" if value["deletion_protection"] else "false",
            )
        )
    if "engine_version" in value:
        pairs.append((f"{key_prefix}EngineVersion", str(value["engine_version"])))
    if "allow_major_version_upgrade" in value:
        pairs.append(
            (
                f"{key_prefix}AllowMajorVersionUpgrade",
                "true" if value["allow_major_version_upgrade"] else "false",
            )
        )


def deserialize_query(el: Element) -> ModifyGlobalClusterMessage:
    out: ModifyGlobalClusterMessage = {}  # type: ignore[typeddict-item]
    child_global_cluster_identifier = el.find("GlobalClusterIdentifier")
    if child_global_cluster_identifier is not None:
        out["global_cluster_identifier"] = str(
            child_global_cluster_identifier.text or ""
        )
    child_new_global_cluster_identifier = el.find("NewGlobalClusterIdentifier")
    if child_new_global_cluster_identifier is not None:
        out["new_global_cluster_identifier"] = str(
            child_new_global_cluster_identifier.text or ""
        )
    child_deletion_protection = el.find("DeletionProtection")
    if child_deletion_protection is not None:
        out["deletion_protection"] = (
            child_deletion_protection.text or ""
        ).lower() == "true"
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_allow_major_version_upgrade = el.find("AllowMajorVersionUpgrade")
    if child_allow_major_version_upgrade is not None:
        out["allow_major_version_upgrade"] = (
            child_allow_major_version_upgrade.text or ""
        ).lower() == "true"
    return out

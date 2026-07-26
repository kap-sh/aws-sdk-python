"""Generated from Smithy shape ``com.amazonaws.docdb#UpgradeTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.boolean
    import capo_docdb.types.string


class UpgradeTarget(TypedDict, closed=True):
    engine: NotRequired["capo_docdb.types.string.String"]
    """<p>The name of the upgrade target database engine.</p>"""
    engine_version: NotRequired["capo_docdb.types.string.String"]
    """<p>The version number of the upgrade target database engine.</p>"""
    description: NotRequired["capo_docdb.types.string.String"]
    """<p>The version of the database engine that an instance can be upgraded to.</p>"""
    auto_upgrade: NotRequired["capo_docdb.types.boolean.Boolean"]
    """<p>A value that indicates whether the target version is applied to any source DB instances that have <code>AutoMinorVersionUpgrade</code> set to <code>true</code>.</p>"""
    is_major_version_upgrade: NotRequired["capo_docdb.types.boolean.Boolean"]
    """<p>A value that indicates whether a database engine is upgraded to a major version.</p>"""


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
    return out

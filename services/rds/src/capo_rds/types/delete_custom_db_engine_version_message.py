"""Generated from Smithy shape ``com.amazonaws.rds#DeleteCustomDBEngineVersionMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.custom_engine_name
    import capo_rds.types.custom_engine_version


class DeleteCustomDBEngineVersionMessage(TypedDict, closed=True):
    engine: NotRequired["capo_rds.types.custom_engine_name.CustomEngineName"]
    """<p>The database engine.</p> <p>RDS Custom for Oracle supports the following values:</p> <ul> <li> <p> <code>custom-oracle-ee</code> </p> </li> <li> <p> <code>custom-oracle-ee-cdb</code> </p> </li> <li> <p> <code>custom-oracle-se2</code> </p> </li> <li> <p> <code>custom-oracle-se2-cdb</code> </p> </li> </ul> <p>RDS Custom for SQL Server supports the following values:</p> <ul> <li> <p> <code>custom-sqlserver-ee</code> </p> </li> <li> <p> <code>custom-sqlserver-se</code> </p> </li> <li> <p> <code>ccustom-sqlserver-web</code> </p> </li> <li> <p> <code>custom-sqlserver-dev</code> </p> </li> </ul> <p>RDS for SQL Server supports only <code>sqlserver-dev-ee</code>.</p>"""
    engine_version: NotRequired[
        "capo_rds.types.custom_engine_version.CustomEngineVersion"
    ]
    """<p>The custom engine version (CEV) for your DB instance. This option is required for RDS Custom, but optional for Amazon RDS. The combination of <code>Engine</code> and <code>EngineVersion</code> is unique per customer per Amazon Web Services Region.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteCustomDBEngineVersionMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "engine" in value:
        pairs.append((f"{key_prefix}Engine", str(value["engine"])))
    if "engine_version" in value:
        pairs.append((f"{key_prefix}EngineVersion", str(value["engine_version"])))


def deserialize_query(el: Element) -> DeleteCustomDBEngineVersionMessage:
    out: DeleteCustomDBEngineVersionMessage = {}  # type: ignore[typeddict-item]
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    return out

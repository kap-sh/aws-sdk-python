"""Generated from Smithy shape ``com.amazonaws.rds#ModifyCustomDBEngineVersionMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.custom_engine_name
    import aws_sdk_rds.types.custom_engine_version
    import aws_sdk_rds.types.custom_engine_version_status
    import aws_sdk_rds.types.description


class ModifyCustomDBEngineVersionMessage(TypedDict):
    engine: NotRequired["aws_sdk_rds.types.custom_engine_name.CustomEngineName"]
    """<p>The database engine.</p> <p>RDS Custom for Oracle supports the following values:</p> <ul> <li> <p> <code>custom-oracle-ee</code> </p> </li> <li> <p> <code>custom-oracle-ee-cdb</code> </p> </li> <li> <p> <code>custom-oracle-se2</code> </p> </li> <li> <p> <code>custom-oracle-se2-cdb</code> </p> </li> </ul> <p>RDS Custom for SQL Server supports the following values:</p> <ul> <li> <p> <code>custom-sqlserver-ee</code> </p> </li> <li> <p> <code>custom-sqlserver-se</code> </p> </li> <li> <p> <code>ccustom-sqlserver-web</code> </p> </li> <li> <p> <code>custom-sqlserver-dev</code> </p> </li> </ul> <p>RDS for SQL Server supports only <code>sqlserver-dev-ee</code>.</p>"""
    engine_version: NotRequired[
        "aws_sdk_rds.types.custom_engine_version.CustomEngineVersion"
    ]
    """<p>The custom engine version (CEV) that you want to modify. This option is required for RDS Custom for Oracle, but optional for Amazon RDS. The combination of <code>Engine</code> and <code>EngineVersion</code> is unique per customer per Amazon Web Services Region.</p>"""
    description: NotRequired["aws_sdk_rds.types.description.Description"]
    """<p>An optional description of your CEV.</p>"""
    status: NotRequired[
        "aws_sdk_rds.types.custom_engine_version_status.CustomEngineVersionStatus"
    ]
    """<p>The availability status to be assigned to the CEV. Valid values are as follows:</p> <dl> <dt>available</dt> <dd> <p>You can use this CEV to create a new RDS Custom DB instance.</p> </dd> <dt>inactive</dt> <dd> <p>You can create a new RDS Custom instance by restoring a DB snapshot with this CEV. You can't patch or create new instances with this CEV.</p> </dd> </dl> <p>You can change any status to any status. A typical reason to change status is to prevent the accidental use of a CEV, or to make a deprecated CEV eligible for use again. For example, you might change the status of your CEV from <code>available</code> to <code>inactive</code>, and from <code>inactive</code> back to <code>available</code>. To change the availability status of the CEV, it must not currently be in use by an RDS Custom instance, snapshot, or automated backup.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyCustomDBEngineVersionMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "engine" in value:
        pairs.append((f"{prefix}.Engine", str(value["engine"])))
    if "engine_version" in value:
        pairs.append((f"{prefix}.EngineVersion", str(value["engine_version"])))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "status" in value:
        import aws_sdk_rds.types.custom_engine_version_status

        aws_sdk_rds.types.custom_engine_version_status.serialize_query(
            value["status"], pairs, f"{prefix}.Status"
        )


def deserialize_query(el: Element) -> ModifyCustomDBEngineVersionMessage:
    out: ModifyCustomDBEngineVersionMessage = {}  # type: ignore[typeddict-item]
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_rds.types.custom_engine_version_status

        out["status"] = (
            aws_sdk_rds.types.custom_engine_version_status.deserialize_query(
                child_status
            )
        )
    return out

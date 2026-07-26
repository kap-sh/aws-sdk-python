"""Generated from Smithy shape ``com.amazonaws.rds#DBParameterGroupStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string


class DBParameterGroupStatus(TypedDict, closed=True):
    db_parameter_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the DB parameter group.</p>"""
    parameter_apply_status: NotRequired["capo_rds.types.string.String"]
    """<p>The status of parameter updates. Valid values are:</p> <ul> <li> <p> <code>applying</code>: The parameter group change is being applied to the database.</p> </li> <li> <p> <code>failed-to-apply</code>: The parameter group is in an invalid state.</p> </li> <li> <p> <code>in-sync</code>: The parameter group change is synchronized with the database.</p> </li> <li> <p> <code>pending-database-upgrade</code>: The parameter group change will be applied after the DB instance is upgraded.</p> </li> <li> <p> <code>pending-reboot</code>: The parameter group change will be applied after the DB instance reboots.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBParameterGroupStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_parameter_group_name" in value:
        pairs.append(
            (f"{prefix}.DBParameterGroupName", str(value["db_parameter_group_name"]))
        )
    if "parameter_apply_status" in value:
        pairs.append(
            (f"{prefix}.ParameterApplyStatus", str(value["parameter_apply_status"]))
        )


def deserialize_query(el: Element) -> DBParameterGroupStatus:
    out: DBParameterGroupStatus = {}  # type: ignore[typeddict-item]
    child_db_parameter_group_name = el.find("DBParameterGroupName")
    if child_db_parameter_group_name is not None:
        out["db_parameter_group_name"] = str(child_db_parameter_group_name.text or "")
    child_parameter_apply_status = el.find("ParameterApplyStatus")
    if child_parameter_apply_status is not None:
        out["parameter_apply_status"] = str(child_parameter_apply_status.text or "")
    return out

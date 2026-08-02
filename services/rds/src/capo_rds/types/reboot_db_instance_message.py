"""Generated from Smithy shape ``com.amazonaws.rds#RebootDBInstanceMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean_optional
    import capo_rds.types.string


class RebootDBInstanceMessage(TypedDict, closed=True):
    db_instance_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The DB instance identifier. This parameter is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing DBInstance.</p> </li> </ul>"""
    force_failover: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether the reboot is conducted through a Multi-AZ failover.</p> <p>Constraint: You can't enable force failover if the instance isn't configured for Multi-AZ.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RebootDBInstanceMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_instance_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBInstanceIdentifier", str(value["db_instance_identifier"]))
        )
    if "force_failover" in value:
        pairs.append(
            (
                f"{key_prefix}ForceFailover",
                "true" if value["force_failover"] else "false",
            )
        )


def deserialize_query(el: Element) -> RebootDBInstanceMessage:
    out: RebootDBInstanceMessage = {}  # type: ignore[typeddict-item]
    child_db_instance_identifier = el.find("DBInstanceIdentifier")
    if child_db_instance_identifier is not None:
        out["db_instance_identifier"] = str(child_db_instance_identifier.text or "")
    child_force_failover = el.find("ForceFailover")
    if child_force_failover is not None:
        out["force_failover"] = (child_force_failover.text or "").lower() == "true"
    return out

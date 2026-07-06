"""Generated from Smithy shape ``com.amazonaws.docdb#RebootDBInstanceMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.boolean_optional
    import aws_sdk_docdb.types.string


class RebootDBInstanceMessage(TypedDict, closed=True):
    db_instance_identifier: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The instance identifier. This parameter is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing <code>DBInstance</code>.</p> </li> </ul>"""
    force_failover: NotRequired["aws_sdk_docdb.types.boolean_optional.BooleanOptional"]
    """<p> When <code>true</code>, the reboot is conducted through a Multi-AZ failover. </p> <p>Constraint: You can't specify <code>true</code> if the instance is not configured for Multi-AZ.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RebootDBInstanceMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_instance_identifier" in value:
        pairs.append(
            (f"{prefix}.DBInstanceIdentifier", str(value["db_instance_identifier"]))
        )
    if "force_failover" in value:
        pairs.append(
            (f"{prefix}.ForceFailover", "true" if value["force_failover"] else "false")
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

"""Generated from Smithy shape ``com.amazonaws.neptune#RebootDBInstanceMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.boolean_optional
    import aws_sdk_neptune.types.string


class RebootDBInstanceMessage(TypedDict):
    db_instance_identifier: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>The DB instance identifier. This parameter is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing DBInstance.</p> </li> </ul>"""
    force_failover: NotRequired[
        "aws_sdk_neptune.types.boolean_optional.BooleanOptional"
    ]
    """<p> When <code>true</code>, the reboot is conducted through a MultiAZ failover.</p> <p>Constraint: You can't specify <code>true</code> if the instance is not configured for MultiAZ.</p>"""


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

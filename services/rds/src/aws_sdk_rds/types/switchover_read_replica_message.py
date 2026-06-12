"""Generated from Smithy shape ``com.amazonaws.rds#SwitchoverReadReplicaMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.string


class SwitchoverReadReplicaMessage(TypedDict):
    db_instance_identifier: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The DB instance identifier of the current standby database. This value is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identiﬁer of an existing Oracle read replica DB instance.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SwitchoverReadReplicaMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_instance_identifier" in value:
        pairs.append(
            (f"{prefix}.DBInstanceIdentifier", str(value["db_instance_identifier"]))
        )


def deserialize_query(el: Element) -> SwitchoverReadReplicaMessage:
    out: SwitchoverReadReplicaMessage = {}  # type: ignore[typeddict-item]
    child_db_instance_identifier = el.find("DBInstanceIdentifier")
    if child_db_instance_identifier is not None:
        out["db_instance_identifier"] = str(child_db_instance_identifier.text or "")
    return out

"""Generated from Smithy shape ``com.amazonaws.rds#StartDBInstanceMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string


class StartDBInstanceMessage(TypedDict, closed=True):
    db_instance_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The user-supplied instance identifier.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StartDBInstanceMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_instance_identifier" in value:
        pairs.append(
            (f"{prefix}.DBInstanceIdentifier", str(value["db_instance_identifier"]))
        )


def deserialize_query(el: Element) -> StartDBInstanceMessage:
    out: StartDBInstanceMessage = {}  # type: ignore[typeddict-item]
    child_db_instance_identifier = el.find("DBInstanceIdentifier")
    if child_db_instance_identifier is not None:
        out["db_instance_identifier"] = str(child_db_instance_identifier.text or "")
    return out

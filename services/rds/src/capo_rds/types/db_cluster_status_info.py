"""Generated from Smithy shape ``com.amazonaws.rds#DBClusterStatusInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean
    import capo_rds.types.string


class DBClusterStatusInfo(TypedDict, closed=True):
    status_type: NotRequired["capo_rds.types.string.String"]
    """<p>Reserved for future use.</p>"""
    normal: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Reserved for future use.</p>"""
    status: NotRequired["capo_rds.types.string.String"]
    """<p>Reserved for future use.</p>"""
    message: NotRequired["capo_rds.types.string.String"]
    """<p>Reserved for future use.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterStatusInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "status_type" in value:
        pairs.append((f"{prefix}.StatusType", str(value["status_type"])))
    if "normal" in value:
        pairs.append((f"{prefix}.Normal", "true" if value["normal"] else "false"))
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))


def deserialize_query(el: Element) -> DBClusterStatusInfo:
    out: DBClusterStatusInfo = {}  # type: ignore[typeddict-item]
    child_status_type = el.find("StatusType")
    if child_status_type is not None:
        out["status_type"] = str(child_status_type.text or "")
    child_normal = el.find("Normal")
    if child_normal is not None:
        out["normal"] = (child_normal.text or "").lower() == "true"
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out

"""Generated from Smithy shape ``com.amazonaws.rds#RecommendedActionUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string


class RecommendedActionUpdate(TypedDict, closed=True):
    action_id: NotRequired["capo_rds.types.string.String"]
    """<p>A unique identifier of the updated recommendation action.</p>"""
    status: NotRequired["capo_rds.types.string.String"]
    """<p>The status of the updated recommendation action.</p> <ul> <li> <p> <code>applied</code> </p> </li> <li> <p> <code>scheduled</code> </p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RecommendedActionUpdate, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "action_id" in value:
        pairs.append((f"{key_prefix}ActionId", str(value["action_id"])))
    if "status" in value:
        pairs.append((f"{key_prefix}Status", str(value["status"])))


def deserialize_query(el: Element) -> RecommendedActionUpdate:
    out: RecommendedActionUpdate = {}  # type: ignore[typeddict-item]
    child_action_id = el.find("ActionId")
    if child_action_id is not None:
        out["action_id"] = str(child_action_id.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    return out

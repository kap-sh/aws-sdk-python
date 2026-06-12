"""Generated from Smithy shape ``com.amazonaws.rds#RecommendedActionUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.string


class RecommendedActionUpdate(TypedDict):
    action_id: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>A unique identifier of the updated recommendation action.</p>"""
    status: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The status of the updated recommendation action.</p> <ul> <li> <p> <code>applied</code> </p> </li> <li> <p> <code>scheduled</code> </p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RecommendedActionUpdate, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "action_id" in value:
        pairs.append((f"{prefix}.ActionId", str(value["action_id"])))
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))


def deserialize_query(el: Element) -> RecommendedActionUpdate:
    out: RecommendedActionUpdate = {}  # type: ignore[typeddict-item]
    child_action_id = el.find("ActionId")
    if child_action_id is not None:
        out["action_id"] = str(child_action_id.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    return out

"""Generated from Smithy shape ``com.amazonaws.elasticache#UpdateActionsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.string
    import capo_elasticache.types.update_action_list


class UpdateActionsMessage(TypedDict, closed=True):
    marker: NotRequired["capo_elasticache.types.string.String"]
    """<p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    update_actions: NotRequired[
        "capo_elasticache.types.update_action_list.UpdateActionList"
    ]
    """<p>Returns a list of update actions</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateActionsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "update_actions" in value:
        import capo_elasticache.types.update_action_list

        capo_elasticache.types.update_action_list.serialize_query(
            value["update_actions"], pairs, f"{key_prefix}UpdateActions"
        )


def deserialize_query(el: Element) -> UpdateActionsMessage:
    out: UpdateActionsMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_update_actions = el.find("UpdateActions")
    if child_update_actions is not None:
        import capo_elasticache.types.update_action_list

        out["update_actions"] = (
            capo_elasticache.types.update_action_list.deserialize_query(
                child_update_actions
            )
        )
    return out

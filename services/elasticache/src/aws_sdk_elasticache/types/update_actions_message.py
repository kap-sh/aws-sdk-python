"""Generated from Smithy shape ``com.amazonaws.elasticache#UpdateActionsMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.string
    import aws_sdk_elasticache.types.update_action_list


class UpdateActionsMessage(TypedDict):
    marker: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    update_actions: NotRequired[
        "aws_sdk_elasticache.types.update_action_list.UpdateActionList"
    ]
    """<p>Returns a list of update actions</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateActionsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "update_actions" in value:
        import aws_sdk_elasticache.types.update_action_list

        aws_sdk_elasticache.types.update_action_list.serialize_query(
            value["update_actions"], pairs, f"{prefix}.UpdateActions"
        )


def deserialize_query(el: Element) -> UpdateActionsMessage:
    out: UpdateActionsMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_update_actions = el.find("UpdateActions")
    if child_update_actions is not None:
        import aws_sdk_elasticache.types.update_action_list

        out["update_actions"] = (
            aws_sdk_elasticache.types.update_action_list.deserialize_query(
                child_update_actions
            )
        )
    return out

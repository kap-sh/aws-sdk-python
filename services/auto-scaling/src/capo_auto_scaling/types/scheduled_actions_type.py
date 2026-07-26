"""Generated from Smithy shape ``com.amazonaws.autoscaling#ScheduledActionsType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.scheduled_update_group_actions
    import capo_auto_scaling.types.xml_string


class ScheduledActionsType(TypedDict, closed=True):
    scheduled_update_group_actions: NotRequired[
        "capo_auto_scaling.types.scheduled_update_group_actions.ScheduledUpdateGroupActions"
    ]
    """<p>The scheduled actions.</p>"""
    next_token: NotRequired["capo_auto_scaling.types.xml_string.XmlString"]
    """<p>A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the <code>NextToken</code> value when requesting the next set of items. This value is null when there are no more items to return.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ScheduledActionsType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "scheduled_update_group_actions" in value:
        import capo_auto_scaling.types.scheduled_update_group_actions

        capo_auto_scaling.types.scheduled_update_group_actions.serialize_query(
            value["scheduled_update_group_actions"],
            pairs,
            f"{prefix}.ScheduledUpdateGroupActions",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ScheduledActionsType:
    out: ScheduledActionsType = {}  # type: ignore[typeddict-item]
    child_scheduled_update_group_actions = el.find("ScheduledUpdateGroupActions")
    if child_scheduled_update_group_actions is not None:
        import capo_auto_scaling.types.scheduled_update_group_actions

        out["scheduled_update_group_actions"] = (
            capo_auto_scaling.types.scheduled_update_group_actions.deserialize_query(
                child_scheduled_update_group_actions
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out

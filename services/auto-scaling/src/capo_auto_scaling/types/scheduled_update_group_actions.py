"""Generated from Smithy shape ``com.amazonaws.autoscaling#ScheduledUpdateGroupActions``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.scheduled_update_group_action

ScheduledUpdateGroupActions: TypeAlias = list[
    "capo_auto_scaling.types.scheduled_update_group_action.ScheduledUpdateGroupAction"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ScheduledUpdateGroupActions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.scheduled_update_group_action

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.scheduled_update_group_action.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ScheduledUpdateGroupActions:
    import capo_auto_scaling.types.scheduled_update_group_action

    out: ScheduledUpdateGroupActions = []
    for child in el.findall("member"):
        out.append(
            capo_auto_scaling.types.scheduled_update_group_action.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: ScheduledUpdateGroupActions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.scheduled_update_group_action

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.scheduled_update_group_action.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ScheduledUpdateGroupActions:
    import capo_auto_scaling.types.scheduled_update_group_action

    out: ScheduledUpdateGroupActions = []
    for child in parent.findall(tag):
        out.append(
            capo_auto_scaling.types.scheduled_update_group_action.deserialize_query(
                child
            )
        )
    return out

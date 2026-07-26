"""Generated from Smithy shape ``com.amazonaws.redshift#ScheduledActionList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.scheduled_action

ScheduledActionList: TypeAlias = list[
    "capo_redshift.types.scheduled_action.ScheduledAction"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ScheduledActionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.scheduled_action

    for n, item in enumerate(value, 1):
        capo_redshift.types.scheduled_action.serialize_query(
            item, pairs, f"{prefix}.ScheduledAction.{n}"
        )


def deserialize_query(el: Element) -> ScheduledActionList:
    import capo_redshift.types.scheduled_action

    out: ScheduledActionList = []
    for child in el.findall("ScheduledAction"):
        out.append(capo_redshift.types.scheduled_action.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ScheduledActionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.scheduled_action

    for n, item in enumerate(value, 1):
        capo_redshift.types.scheduled_action.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ScheduledActionList:
    import capo_redshift.types.scheduled_action

    out: ScheduledActionList = []
    for child in parent.findall(tag):
        out.append(capo_redshift.types.scheduled_action.deserialize_query(child))
    return out

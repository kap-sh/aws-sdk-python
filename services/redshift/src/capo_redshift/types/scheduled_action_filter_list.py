"""Generated from Smithy shape ``com.amazonaws.redshift#ScheduledActionFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.scheduled_action_filter

ScheduledActionFilterList: TypeAlias = list[
    "capo_redshift.types.scheduled_action_filter.ScheduledActionFilter"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ScheduledActionFilterList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.scheduled_action_filter

    for n, item in enumerate(value, 1):
        capo_redshift.types.scheduled_action_filter.serialize_query(
            item, pairs, f"{prefix}.ScheduledActionFilter.{n}"
        )


def deserialize_query(el: Element) -> ScheduledActionFilterList:
    import capo_redshift.types.scheduled_action_filter

    out: ScheduledActionFilterList = []
    for child in el.findall("ScheduledActionFilter"):
        out.append(capo_redshift.types.scheduled_action_filter.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ScheduledActionFilterList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.scheduled_action_filter

    for n, item in enumerate(value, 1):
        capo_redshift.types.scheduled_action_filter.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ScheduledActionFilterList:
    import capo_redshift.types.scheduled_action_filter

    out: ScheduledActionFilterList = []
    for child in parent.findall(tag):
        out.append(capo_redshift.types.scheduled_action_filter.deserialize_query(child))
    return out

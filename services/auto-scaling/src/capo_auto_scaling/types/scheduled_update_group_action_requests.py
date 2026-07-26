"""Generated from Smithy shape ``com.amazonaws.autoscaling#ScheduledUpdateGroupActionRequests``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.scheduled_update_group_action_request

ScheduledUpdateGroupActionRequests: TypeAlias = list[
    "capo_auto_scaling.types.scheduled_update_group_action_request.ScheduledUpdateGroupActionRequest"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ScheduledUpdateGroupActionRequests, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.scheduled_update_group_action_request

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.scheduled_update_group_action_request.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ScheduledUpdateGroupActionRequests:
    import capo_auto_scaling.types.scheduled_update_group_action_request

    out: ScheduledUpdateGroupActionRequests = []
    for child in el.findall("member"):
        out.append(
            capo_auto_scaling.types.scheduled_update_group_action_request.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: ScheduledUpdateGroupActionRequests, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.scheduled_update_group_action_request

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.scheduled_update_group_action_request.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> ScheduledUpdateGroupActionRequests:
    import capo_auto_scaling.types.scheduled_update_group_action_request

    out: ScheduledUpdateGroupActionRequests = []
    for child in parent.findall(tag):
        out.append(
            capo_auto_scaling.types.scheduled_update_group_action_request.deserialize_query(
                child
            )
        )
    return out

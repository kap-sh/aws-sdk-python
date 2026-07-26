"""Generated from Smithy shape ``com.amazonaws.autoscaling#FailedScheduledUpdateGroupActionRequests``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.failed_scheduled_update_group_action_request

FailedScheduledUpdateGroupActionRequests: TypeAlias = list[
    "capo_auto_scaling.types.failed_scheduled_update_group_action_request.FailedScheduledUpdateGroupActionRequest"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: FailedScheduledUpdateGroupActionRequests,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import capo_auto_scaling.types.failed_scheduled_update_group_action_request

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.failed_scheduled_update_group_action_request.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> FailedScheduledUpdateGroupActionRequests:
    import capo_auto_scaling.types.failed_scheduled_update_group_action_request

    out: FailedScheduledUpdateGroupActionRequests = []
    for child in el.findall("member"):
        out.append(
            capo_auto_scaling.types.failed_scheduled_update_group_action_request.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: FailedScheduledUpdateGroupActionRequests,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import capo_auto_scaling.types.failed_scheduled_update_group_action_request

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.failed_scheduled_update_group_action_request.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> FailedScheduledUpdateGroupActionRequests:
    import capo_auto_scaling.types.failed_scheduled_update_group_action_request

    out: FailedScheduledUpdateGroupActionRequests = []
    for child in parent.findall(tag):
        out.append(
            capo_auto_scaling.types.failed_scheduled_update_group_action_request.deserialize_query(
                child
            )
        )
    return out

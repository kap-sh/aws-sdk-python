"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceEventWindow``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_event_window_association_target
    import capo_ec2.types.instance_event_window_cron_expression
    import capo_ec2.types.instance_event_window_id
    import capo_ec2.types.instance_event_window_state
    import capo_ec2.types.instance_event_window_time_range_list
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class InstanceEventWindow(TypedDict, closed=True):
    instance_event_window_id: NotRequired[
        "capo_ec2.types.instance_event_window_id.InstanceEventWindowId"
    ]
    """<p>The ID of the event window.</p>"""
    time_ranges: NotRequired[
        "capo_ec2.types.instance_event_window_time_range_list.InstanceEventWindowTimeRangeList"
    ]
    """<p>One or more time ranges defined for the event window.</p>"""
    name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the event window.</p>"""
    cron_expression: NotRequired[
        "capo_ec2.types.instance_event_window_cron_expression.InstanceEventWindowCronExpression"
    ]
    """<p>The cron expression defined for the event window.</p>"""
    association_target: NotRequired[
        "capo_ec2.types.instance_event_window_association_target.InstanceEventWindowAssociationTarget"
    ]
    """<p>One or more targets associated with the event window.</p>"""
    state: NotRequired[
        "capo_ec2.types.instance_event_window_state.InstanceEventWindowState"
    ]
    """<p>The current state of the event window.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The instance tags associated with the event window.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceEventWindow, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_event_window_id" in value:
        pairs.append(
            (
                f"{key_prefix}InstanceEventWindowId",
                str(value["instance_event_window_id"]),
            )
        )
    if "time_ranges" in value:
        import capo_ec2.types.instance_event_window_time_range_list

        capo_ec2.types.instance_event_window_time_range_list.serialize_ec2_query(
            value["time_ranges"], pairs, f"{key_prefix}TimeRangeSet"
        )
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))
    if "cron_expression" in value:
        pairs.append((f"{key_prefix}CronExpression", str(value["cron_expression"])))
    if "association_target" in value:
        import capo_ec2.types.instance_event_window_association_target

        capo_ec2.types.instance_event_window_association_target.serialize_ec2_query(
            value["association_target"], pairs, f"{key_prefix}AssociationTarget"
        )
    if "state" in value:
        import capo_ec2.types.instance_event_window_state

        capo_ec2.types.instance_event_window_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )


def deserialize_ec2_query(el: Element) -> InstanceEventWindow:
    out: InstanceEventWindow = {}  # type: ignore[typeddict-item]
    child_instance_event_window_id = el.find("instanceEventWindowId")
    if child_instance_event_window_id is not None:
        out["instance_event_window_id"] = str(child_instance_event_window_id.text or "")
    child_time_ranges = el.find("timeRangeSet")
    if child_time_ranges is not None:
        import capo_ec2.types.instance_event_window_time_range_list

        out["time_ranges"] = (
            capo_ec2.types.instance_event_window_time_range_list.deserialize_ec2_query(
                child_time_ranges
            )
        )
    child_name = el.find("name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_cron_expression = el.find("cronExpression")
    if child_cron_expression is not None:
        out["cron_expression"] = str(child_cron_expression.text or "")
    child_association_target = el.find("associationTarget")
    if child_association_target is not None:
        import capo_ec2.types.instance_event_window_association_target

        out["association_target"] = (
            capo_ec2.types.instance_event_window_association_target.deserialize_ec2_query(
                child_association_target
            )
        )
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.instance_event_window_state

        out["state"] = capo_ec2.types.instance_event_window_state.deserialize_ec2_query(
            child_state
        )
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    return out

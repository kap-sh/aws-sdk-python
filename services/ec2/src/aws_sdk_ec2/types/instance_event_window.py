"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceEventWindow``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_event_window_association_target
    import aws_sdk_ec2.types.instance_event_window_cron_expression
    import aws_sdk_ec2.types.instance_event_window_id
    import aws_sdk_ec2.types.instance_event_window_state
    import aws_sdk_ec2.types.instance_event_window_time_range_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class InstanceEventWindow(TypedDict):
    instance_event_window_id: NotRequired[
        "aws_sdk_ec2.types.instance_event_window_id.InstanceEventWindowId"
    ]
    """<p>The ID of the event window.</p>"""
    time_ranges: NotRequired[
        "aws_sdk_ec2.types.instance_event_window_time_range_list.InstanceEventWindowTimeRangeList"
    ]
    """<p>One or more time ranges defined for the event window.</p>"""
    name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the event window.</p>"""
    cron_expression: NotRequired[
        "aws_sdk_ec2.types.instance_event_window_cron_expression.InstanceEventWindowCronExpression"
    ]
    """<p>The cron expression defined for the event window.</p>"""
    association_target: NotRequired[
        "aws_sdk_ec2.types.instance_event_window_association_target.InstanceEventWindowAssociationTarget"
    ]
    """<p>One or more targets associated with the event window.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.instance_event_window_state.InstanceEventWindowState"
    ]
    """<p>The current state of the event window.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The instance tags associated with the event window.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceEventWindow, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "instance_event_window_id" in value:
        pairs.append(
            (f"{prefix}.InstanceEventWindowId", str(value["instance_event_window_id"]))
        )
    if "time_ranges" in value:
        import aws_sdk_ec2.types.instance_event_window_time_range_list

        aws_sdk_ec2.types.instance_event_window_time_range_list.serialize_ec2_query(
            value["time_ranges"], pairs, f"{prefix}.TimeRangeSet"
        )
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))
    if "cron_expression" in value:
        pairs.append((f"{prefix}.CronExpression", str(value["cron_expression"])))
    if "association_target" in value:
        import aws_sdk_ec2.types.instance_event_window_association_target

        aws_sdk_ec2.types.instance_event_window_association_target.serialize_ec2_query(
            value["association_target"], pairs, f"{prefix}.AssociationTarget"
        )
    if "state" in value:
        import aws_sdk_ec2.types.instance_event_window_state

        aws_sdk_ec2.types.instance_event_window_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )


def deserialize_ec2_query(el: Element) -> InstanceEventWindow:
    out: InstanceEventWindow = {}  # type: ignore[typeddict-item]
    child_instance_event_window_id = el.find("InstanceEventWindowId")
    if child_instance_event_window_id is not None:
        out["instance_event_window_id"] = str(child_instance_event_window_id.text or "")
    if el.find("TimeRangeSet") is not None:
        import aws_sdk_ec2.types.instance_event_window_time_range_list

        out["time_ranges"] = (
            aws_sdk_ec2.types.instance_event_window_time_range_list.deserialize_ec2_query(
                el, "TimeRangeSet"
            )
        )
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_cron_expression = el.find("CronExpression")
    if child_cron_expression is not None:
        out["cron_expression"] = str(child_cron_expression.text or "")
    child_association_target = el.find("AssociationTarget")
    if child_association_target is not None:
        import aws_sdk_ec2.types.instance_event_window_association_target

        out["association_target"] = (
            aws_sdk_ec2.types.instance_event_window_association_target.deserialize_ec2_query(
                child_association_target
            )
        )
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.instance_event_window_state

        out["state"] = (
            aws_sdk_ec2.types.instance_event_window_state.deserialize_ec2_query(
                child_state
            )
        )
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out

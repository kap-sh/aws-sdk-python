"""Generated from Smithy shape ``com.amazonaws.autoscaling#Activity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.auto_scaling_group_state
    import capo_auto_scaling.types.progress
    import capo_auto_scaling.types.resource_name
    import capo_auto_scaling.types.scaling_activity_status_code
    import capo_auto_scaling.types.timestamp_type
    import capo_auto_scaling.types.xml_string
    import capo_auto_scaling.types.xml_string_max_len255
    import capo_auto_scaling.types.xml_string_max_len1023


class Activity(TypedDict, closed=True):
    activity_id: NotRequired["capo_auto_scaling.types.xml_string.XmlString"]
    """<p>The ID of the activity.</p>"""
    auto_scaling_group_name: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the Auto Scaling group.</p>"""
    description: NotRequired["capo_auto_scaling.types.xml_string.XmlString"]
    """<p>A friendly, more verbose description of the activity.</p>"""
    cause: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len1023.XmlStringMaxLen1023"
    ]
    """<p>The reason the activity began.</p>"""
    start_time: NotRequired["capo_auto_scaling.types.timestamp_type.TimestampType"]
    """<p>The start time of the activity.</p>"""
    end_time: NotRequired["capo_auto_scaling.types.timestamp_type.TimestampType"]
    """<p>The end time of the activity.</p>"""
    status_code: NotRequired[
        "capo_auto_scaling.types.scaling_activity_status_code.ScalingActivityStatusCode"
    ]
    """<p>The current status of the activity.</p>"""
    status_message: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>A friendly, more verbose description of the activity status.</p>"""
    progress: NotRequired["capo_auto_scaling.types.progress.Progress"]
    """<p>A value between 0 and 100 that indicates the progress of the activity.</p>"""
    details: NotRequired["capo_auto_scaling.types.xml_string.XmlString"]
    """<p>The details about the activity.</p>"""
    auto_scaling_group_state: NotRequired[
        "capo_auto_scaling.types.auto_scaling_group_state.AutoScalingGroupState"
    ]
    """<p>The state of the Auto Scaling group, which is either <code>InService</code> or <code>Deleted</code>.</p>"""
    auto_scaling_group_arn: NotRequired[
        "capo_auto_scaling.types.resource_name.ResourceName"
    ]
    """<p>The Amazon Resource Name (ARN) of the Auto Scaling group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Activity, pairs: list[tuple[str, str]], prefix: str) -> None:
    if "activity_id" in value:
        pairs.append((f"{prefix}.ActivityId", str(value["activity_id"])))
    if "auto_scaling_group_name" in value:
        pairs.append(
            (f"{prefix}.AutoScalingGroupName", str(value["auto_scaling_group_name"]))
        )
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "cause" in value:
        pairs.append((f"{prefix}.Cause", str(value["cause"])))
    if "start_time" in value:
        import capo_auto_scaling.types.timestamp_type

        capo_auto_scaling.types.timestamp_type.serialize_query(
            value["start_time"], pairs, f"{prefix}.StartTime"
        )
    if "end_time" in value:
        import capo_auto_scaling.types.timestamp_type

        capo_auto_scaling.types.timestamp_type.serialize_query(
            value["end_time"], pairs, f"{prefix}.EndTime"
        )
    if "status_code" in value:
        import capo_auto_scaling.types.scaling_activity_status_code

        capo_auto_scaling.types.scaling_activity_status_code.serialize_query(
            value["status_code"], pairs, f"{prefix}.StatusCode"
        )
    if "status_message" in value:
        pairs.append((f"{prefix}.StatusMessage", str(value["status_message"])))
    if "progress" in value:
        pairs.append((f"{prefix}.Progress", str(value["progress"])))
    if "details" in value:
        pairs.append((f"{prefix}.Details", str(value["details"])))
    if "auto_scaling_group_state" in value:
        pairs.append(
            (f"{prefix}.AutoScalingGroupState", str(value["auto_scaling_group_state"]))
        )
    if "auto_scaling_group_arn" in value:
        pairs.append(
            (f"{prefix}.AutoScalingGroupARN", str(value["auto_scaling_group_arn"]))
        )


def deserialize_query(el: Element) -> Activity:
    out: Activity = {}  # type: ignore[typeddict-item]
    child_activity_id = el.find("ActivityId")
    if child_activity_id is not None:
        out["activity_id"] = str(child_activity_id.text or "")
    child_auto_scaling_group_name = el.find("AutoScalingGroupName")
    if child_auto_scaling_group_name is not None:
        out["auto_scaling_group_name"] = str(child_auto_scaling_group_name.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_cause = el.find("Cause")
    if child_cause is not None:
        out["cause"] = str(child_cause.text or "")
    child_start_time = el.find("StartTime")
    if child_start_time is not None:
        import capo_auto_scaling.types.timestamp_type

        out["start_time"] = capo_auto_scaling.types.timestamp_type.deserialize_query(
            child_start_time
        )
    child_end_time = el.find("EndTime")
    if child_end_time is not None:
        import capo_auto_scaling.types.timestamp_type

        out["end_time"] = capo_auto_scaling.types.timestamp_type.deserialize_query(
            child_end_time
        )
    child_status_code = el.find("StatusCode")
    if child_status_code is not None:
        import capo_auto_scaling.types.scaling_activity_status_code

        out["status_code"] = (
            capo_auto_scaling.types.scaling_activity_status_code.deserialize_query(
                child_status_code
            )
        )
    child_status_message = el.find("StatusMessage")
    if child_status_message is not None:
        out["status_message"] = str(child_status_message.text or "")
    child_progress = el.find("Progress")
    if child_progress is not None:
        out["progress"] = int(child_progress.text or "")
    child_details = el.find("Details")
    if child_details is not None:
        out["details"] = str(child_details.text or "")
    child_auto_scaling_group_state = el.find("AutoScalingGroupState")
    if child_auto_scaling_group_state is not None:
        out["auto_scaling_group_state"] = str(child_auto_scaling_group_state.text or "")
    child_auto_scaling_group_arn = el.find("AutoScalingGroupARN")
    if child_auto_scaling_group_arn is not None:
        out["auto_scaling_group_arn"] = str(child_auto_scaling_group_arn.text or "")
    return out

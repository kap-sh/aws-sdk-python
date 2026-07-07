"""Generated from Smithy shape ``com.amazonaws.swf#RegisterActivityTypeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.description
    import aws_sdk_swf.types.domain_name
    import aws_sdk_swf.types.duration_in_seconds_optional
    import aws_sdk_swf.types.name
    import aws_sdk_swf.types.task_list
    import aws_sdk_swf.types.task_priority
    import aws_sdk_swf.types.version


class RegisterActivityTypeInput(TypedDict, closed=True):
    domain: "aws_sdk_swf.types.domain_name.DomainName"
    """<p>The name of the domain in which this activity is to be registered.</p>"""
    name: "aws_sdk_swf.types.name.Name"
    r"""<p>The name of the activity type within the domain.</p> <p>The specified string must not contain a <code>:</code> (colon), <code>/</code> (slash), <code>|</code> (vertical bar), or any control characters (<code>\u0000-\u001f</code> | <code>\u007f-\u009f</code>). Also, it must <i>not</i> be the literal string <code>arn</code>.</p>"""
    version: "aws_sdk_swf.types.version.Version"
    r"""<p>The version of the activity type.</p> <note> <p>The activity type consists of the name and version, the combination of which must be unique within the domain.</p> </note> <p>The specified string must not contain a <code>:</code> (colon), <code>/</code> (slash), <code>|</code> (vertical bar), or any control characters (<code>\u0000-\u001f</code> | <code>\u007f-\u009f</code>). Also, it must <i>not</i> be the literal string <code>arn</code>.</p>"""
    description: NotRequired["aws_sdk_swf.types.description.Description"]
    """<p>A textual description of the activity type.</p>"""
    default_task_start_to_close_timeout: NotRequired[
        "aws_sdk_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
    ]
    """<p>If set, specifies the default maximum duration that a worker can take to process tasks of this activity type. This default can be overridden when scheduling an activity task using the <code>ScheduleActivityTask</code> <a>Decision</a>.</p> <p>The duration is specified in seconds, an integer greater than or equal to <code>0</code>. You can use <code>NONE</code> to specify unlimited duration.</p>"""
    default_task_heartbeat_timeout: NotRequired[
        "aws_sdk_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
    ]
    """<p>If set, specifies the default maximum time before which a worker processing a task of this type must report progress by calling <a>RecordActivityTaskHeartbeat</a>. If the timeout is exceeded, the activity task is automatically timed out. This default can be overridden when scheduling an activity task using the <code>ScheduleActivityTask</code> <a>Decision</a>. If the activity worker subsequently attempts to record a heartbeat or returns a result, the activity worker receives an <code>UnknownResource</code> fault. In this case, Amazon SWF no longer considers the activity task to be valid; the activity worker should clean up the activity task.</p> <p>The duration is specified in seconds, an integer greater than or equal to <code>0</code>. You can use <code>NONE</code> to specify unlimited duration.</p>"""
    default_task_list: NotRequired["aws_sdk_swf.types.task_list.TaskList"]
    """<p>If set, specifies the default task list to use for scheduling tasks of this activity type. This default task list is used if a task list isn't provided when a task is scheduled through the <code>ScheduleActivityTask</code> <a>Decision</a>.</p>"""
    default_task_priority: NotRequired["aws_sdk_swf.types.task_priority.TaskPriority"]
    r"""<p>The default task priority to assign to the activity type. If not assigned, then <code>0</code> is used. Valid values are integers that range from Java's <code>Integer.MIN_VALUE</code> (-2147483648) to <code>Integer.MAX_VALUE</code> (2147483647). Higher numbers indicate higher priority.</p> <p>For more information about setting task priority, see <a href=\"https://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-priority.html\">Setting Task Priority</a> in the <i>in the <i>Amazon SWF Developer Guide</i>.</i>.</p>"""
    default_task_schedule_to_start_timeout: NotRequired[
        "aws_sdk_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
    ]
    """<p>If set, specifies the default maximum duration that a task of this activity type can wait before being assigned to a worker. This default can be overridden when scheduling an activity task using the <code>ScheduleActivityTask</code> <a>Decision</a>.</p> <p>The duration is specified in seconds, an integer greater than or equal to <code>0</code>. You can use <code>NONE</code> to specify unlimited duration.</p>"""
    default_task_schedule_to_close_timeout: NotRequired[
        "aws_sdk_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
    ]
    """<p>If set, specifies the default maximum duration for a task of this activity type. This default can be overridden when scheduling an activity task using the <code>ScheduleActivityTask</code> <a>Decision</a>.</p> <p>The duration is specified in seconds, an integer greater than or equal to <code>0</code>. You can use <code>NONE</code> to specify unlimited duration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegisterActivityTypeInput) -> dict:
    out: dict = {}
    out["domain"] = value["domain"]
    out["name"] = value["name"]
    out["version"] = value["version"]
    if "description" in value:
        out["description"] = value["description"]
    if "default_task_start_to_close_timeout" in value:
        out["defaultTaskStartToCloseTimeout"] = value[
            "default_task_start_to_close_timeout"
        ]
    if "default_task_heartbeat_timeout" in value:
        out["defaultTaskHeartbeatTimeout"] = value["default_task_heartbeat_timeout"]
    if "default_task_list" in value:
        import aws_sdk_swf.types.task_list

        out["defaultTaskList"] = aws_sdk_swf.types.task_list.serialize_aws_json_1_0(
            value["default_task_list"]
        )
    if "default_task_priority" in value:
        out["defaultTaskPriority"] = value["default_task_priority"]
    if "default_task_schedule_to_start_timeout" in value:
        out["defaultTaskScheduleToStartTimeout"] = value[
            "default_task_schedule_to_start_timeout"
        ]
    if "default_task_schedule_to_close_timeout" in value:
        out["defaultTaskScheduleToCloseTimeout"] = value[
            "default_task_schedule_to_close_timeout"
        ]
    return out


def deserialize_aws_json_1_0(data: dict) -> RegisterActivityTypeInput:
    out: RegisterActivityTypeInput = {}  # type: ignore[typeddict-item]
    if "domain" in data:
        out["domain"] = data["domain"]
    else:
        raise DeserializationError("RegisterActivityTypeInput.domain required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("RegisterActivityTypeInput.name required")
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError("RegisterActivityTypeInput.version required")
    if "description" in data:
        out["description"] = data["description"]
    if "defaultTaskStartToCloseTimeout" in data:
        out["default_task_start_to_close_timeout"] = data[
            "defaultTaskStartToCloseTimeout"
        ]
    if "defaultTaskHeartbeatTimeout" in data:
        out["default_task_heartbeat_timeout"] = data["defaultTaskHeartbeatTimeout"]
    if "defaultTaskList" in data:
        import aws_sdk_swf.types.task_list

        out["default_task_list"] = aws_sdk_swf.types.task_list.deserialize_aws_json_1_0(
            data["defaultTaskList"]
        )
    if "defaultTaskPriority" in data:
        out["default_task_priority"] = data["defaultTaskPriority"]
    if "defaultTaskScheduleToStartTimeout" in data:
        out["default_task_schedule_to_start_timeout"] = data[
            "defaultTaskScheduleToStartTimeout"
        ]
    if "defaultTaskScheduleToCloseTimeout" in data:
        out["default_task_schedule_to_close_timeout"] = data[
            "defaultTaskScheduleToCloseTimeout"
        ]
    return out

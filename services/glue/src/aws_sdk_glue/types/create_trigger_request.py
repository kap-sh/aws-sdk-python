"""Generated from Smithy shape ``com.amazonaws.glue#CreateTriggerRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.action_list
    import aws_sdk_glue.types.boolean_value
    import aws_sdk_glue.types.description_string
    import aws_sdk_glue.types.event_batching_condition
    import aws_sdk_glue.types.generic_string
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.predicate
    import aws_sdk_glue.types.tags_map
    import aws_sdk_glue.types.trigger_type


class CreateTriggerRequest(TypedDict):
    name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the trigger.</p>"""
    workflow_name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name of the workflow associated with the trigger.</p>"""
    type: "aws_sdk_glue.types.trigger_type.TriggerType"
    """<p>The type of the new trigger.</p>"""
    schedule: NotRequired["aws_sdk_glue.types.generic_string.GenericString"]
    r"""<p>A <code>cron</code> expression used to specify the schedule (see <a href=\"https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html\">Time-Based Schedules for Jobs and Crawlers</a>. For example, to run something every day at 12:15 UTC, you would specify: <code>cron(15 12 * * ? *)</code>.</p> <p>This field is required when the trigger type is SCHEDULED.</p>"""
    predicate: NotRequired["aws_sdk_glue.types.predicate.Predicate"]
    """<p>A predicate to specify when the new trigger should fire.</p> <p>This field is required when the trigger type is <code>CONDITIONAL</code>.</p>"""
    actions: "aws_sdk_glue.types.action_list.ActionList"
    """<p>The actions initiated by this trigger when it fires.</p>"""
    description: NotRequired["aws_sdk_glue.types.description_string.DescriptionString"]
    """<p>A description of the new trigger.</p>"""
    start_on_creation: "aws_sdk_glue.types.boolean_value.BooleanValue"
    """<p>Set to <code>true</code> to start <code>SCHEDULED</code> and <code>CONDITIONAL</code> triggers when created. True is not supported for <code>ON_DEMAND</code> triggers.</p>"""
    tags: NotRequired["aws_sdk_glue.types.tags_map.TagsMap"]
    r"""<p>The tags to use with this trigger. You may use tags to limit access to the trigger. For more information about tags in Glue, see <a href=\"https://docs.aws.amazon.com/glue/latest/dg/monitor-tags.html\">Amazon Web Services Tags in Glue</a> in the developer guide. </p>"""
    event_batching_condition: NotRequired[
        "aws_sdk_glue.types.event_batching_condition.EventBatchingCondition"
    ]
    """<p>Batch condition that must be met (specified number of events received or batch time window expired) before EventBridge event trigger fires.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTriggerRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "workflow_name" in value:
        out["WorkflowName"] = value["workflow_name"]
    import aws_sdk_glue.types.trigger_type

    out["Type"] = aws_sdk_glue.types.trigger_type.serialize_aws_json_1_1(value["type"])
    if "schedule" in value:
        out["Schedule"] = value["schedule"]
    if "predicate" in value:
        import aws_sdk_glue.types.predicate

        out["Predicate"] = aws_sdk_glue.types.predicate.serialize_aws_json_1_1(
            value["predicate"]
        )
    import aws_sdk_glue.types.action_list

    out["Actions"] = aws_sdk_glue.types.action_list.serialize_aws_json_1_1(
        value["actions"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    out["StartOnCreation"] = value.get("start_on_creation", False)
    if "tags" in value:
        import aws_sdk_glue.types.tags_map

        out["Tags"] = aws_sdk_glue.types.tags_map.serialize_aws_json_1_1(value["tags"])
    if "event_batching_condition" in value:
        import aws_sdk_glue.types.event_batching_condition

        out["EventBatchingCondition"] = (
            aws_sdk_glue.types.event_batching_condition.serialize_aws_json_1_1(
                value["event_batching_condition"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTriggerRequest:
    out: CreateTriggerRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateTriggerRequest.name required")
    if "WorkflowName" in data:
        out["workflow_name"] = data["WorkflowName"]
    if "Type" in data:
        import aws_sdk_glue.types.trigger_type

        out["type"] = aws_sdk_glue.types.trigger_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        raise DeserializationError("CreateTriggerRequest.type required")
    if "Schedule" in data:
        out["schedule"] = data["Schedule"]
    if "Predicate" in data:
        import aws_sdk_glue.types.predicate

        out["predicate"] = aws_sdk_glue.types.predicate.deserialize_aws_json_1_1(
            data["Predicate"]
        )
    if "Actions" in data:
        import aws_sdk_glue.types.action_list

        out["actions"] = aws_sdk_glue.types.action_list.deserialize_aws_json_1_1(
            data["Actions"]
        )
    else:
        raise DeserializationError("CreateTriggerRequest.actions required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "StartOnCreation" in data:
        out["start_on_creation"] = data["StartOnCreation"]
    else:
        out["start_on_creation"] = False
    if "Tags" in data:
        import aws_sdk_glue.types.tags_map

        out["tags"] = aws_sdk_glue.types.tags_map.deserialize_aws_json_1_1(data["Tags"])
    if "EventBatchingCondition" in data:
        import aws_sdk_glue.types.event_batching_condition

        out["event_batching_condition"] = (
            aws_sdk_glue.types.event_batching_condition.deserialize_aws_json_1_1(
                data["EventBatchingCondition"]
            )
        )
    return out

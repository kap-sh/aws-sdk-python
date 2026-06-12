"""Generated from Smithy shape ``com.amazonaws.connect#Rule``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.rule_actions
    import aws_sdk_connect.types.rule_function
    import aws_sdk_connect.types.rule_id
    import aws_sdk_connect.types.rule_name
    import aws_sdk_connect.types.rule_publish_status
    import aws_sdk_connect.types.rule_trigger_event_source
    import aws_sdk_connect.types.tag_map
    import aws_sdk_connect.types.timestamp


class Rule(TypedDict):
    name: "aws_sdk_connect.types.rule_name.RuleName"
    """<p>The name of the rule.</p>"""
    rule_id: "aws_sdk_connect.types.rule_id.RuleId"
    """<p>A unique identifier for the rule.</p>"""
    rule_arn: "aws_sdk_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the rule.</p>"""
    trigger_event_source: (
        "aws_sdk_connect.types.rule_trigger_event_source.RuleTriggerEventSource"
    )
    """<p>The event source to trigger the rule.</p>"""
    function: "aws_sdk_connect.types.rule_function.RuleFunction"
    """<p>The conditions of the rule.</p>"""
    actions: "aws_sdk_connect.types.rule_actions.RuleActions"
    """<p>A list of actions to be run when the rule is triggered.</p>"""
    publish_status: "aws_sdk_connect.types.rule_publish_status.RulePublishStatus"
    """<p>The publish status of the rule.</p>"""
    created_time: "aws_sdk_connect.types.timestamp.Timestamp"
    """<p>The timestamp for when the rule was created.</p>"""
    last_updated_time: "aws_sdk_connect.types.timestamp.Timestamp"
    """<p>The timestamp for the when the rule was last updated.</p>"""
    last_updated_by: "aws_sdk_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the user who last updated the rule.</p>"""
    tags: NotRequired["aws_sdk_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { \"Tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Rule) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["RuleId"] = value["rule_id"]
    out["RuleArn"] = value["rule_arn"]
    import aws_sdk_connect.types.rule_trigger_event_source

    out["TriggerEventSource"] = (
        aws_sdk_connect.types.rule_trigger_event_source.serialize_json(
            value["trigger_event_source"]
        )
    )
    out["Function"] = value["function"]
    import aws_sdk_connect.types.rule_actions

    out["Actions"] = aws_sdk_connect.types.rule_actions.serialize_json(value["actions"])
    import aws_sdk_connect.types.rule_publish_status

    out["PublishStatus"] = aws_sdk_connect.types.rule_publish_status.serialize_json(
        value["publish_status"]
    )
    import aws_sdk_connect.types.timestamp

    out["CreatedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
        value["created_time"]
    )
    import aws_sdk_connect.types.timestamp

    out["LastUpdatedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
        value["last_updated_time"]
    )
    out["LastUpdatedBy"] = value["last_updated_by"]
    if "tags" in value:
        import aws_sdk_connect.types.tag_map

        out["Tags"] = aws_sdk_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> Rule:
    out: Rule = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Rule.name required")
    if "RuleId" in data:
        out["rule_id"] = data["RuleId"]
    else:
        raise DeserializationError("Rule.rule_id required")
    if "RuleArn" in data:
        out["rule_arn"] = data["RuleArn"]
    else:
        raise DeserializationError("Rule.rule_arn required")
    if "TriggerEventSource" in data:
        import aws_sdk_connect.types.rule_trigger_event_source

        out["trigger_event_source"] = (
            aws_sdk_connect.types.rule_trigger_event_source.deserialize_json(
                data["TriggerEventSource"]
            )
        )
    else:
        raise DeserializationError("Rule.trigger_event_source required")
    if "Function" in data:
        out["function"] = data["Function"]
    else:
        raise DeserializationError("Rule.function required")
    if "Actions" in data:
        import aws_sdk_connect.types.rule_actions

        out["actions"] = aws_sdk_connect.types.rule_actions.deserialize_json(
            data["Actions"]
        )
    else:
        raise DeserializationError("Rule.actions required")
    if "PublishStatus" in data:
        import aws_sdk_connect.types.rule_publish_status

        out["publish_status"] = (
            aws_sdk_connect.types.rule_publish_status.deserialize_json(
                data["PublishStatus"]
            )
        )
    else:
        raise DeserializationError("Rule.publish_status required")
    if "CreatedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["created_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    else:
        raise DeserializationError("Rule.created_time required")
    if "LastUpdatedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["last_updated_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    else:
        raise DeserializationError("Rule.last_updated_time required")
    if "LastUpdatedBy" in data:
        out["last_updated_by"] = data["LastUpdatedBy"]
    else:
        raise DeserializationError("Rule.last_updated_by required")
    if "Tags" in data:
        import aws_sdk_connect.types.tag_map

        out["tags"] = aws_sdk_connect.types.tag_map.deserialize_json(data["Tags"])
    return out

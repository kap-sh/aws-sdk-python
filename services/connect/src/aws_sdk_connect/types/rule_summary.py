"""Generated from Smithy shape ``com.amazonaws.connect#RuleSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.action_summaries
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.event_source_name
    import aws_sdk_connect.types.rule_id
    import aws_sdk_connect.types.rule_name
    import aws_sdk_connect.types.rule_publish_status
    import aws_sdk_connect.types.timestamp


class RuleSummary(TypedDict, closed=True):
    name: "aws_sdk_connect.types.rule_name.RuleName"
    """<p>The name of the rule.</p>"""
    rule_id: "aws_sdk_connect.types.rule_id.RuleId"
    """<p>A unique identifier for the rule.</p>"""
    rule_arn: "aws_sdk_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the rule.</p>"""
    event_source_name: "aws_sdk_connect.types.event_source_name.EventSourceName"
    """<p>The name of the event source.</p>"""
    publish_status: "aws_sdk_connect.types.rule_publish_status.RulePublishStatus"
    """<p>The publish status of the rule.</p>"""
    action_summaries: "aws_sdk_connect.types.action_summaries.ActionSummaries"
    """<p>A list of ActionTypes associated with a rule. </p>"""
    created_time: "aws_sdk_connect.types.timestamp.Timestamp"
    """<p>The timestamp for when the rule was created. </p>"""
    last_updated_time: "aws_sdk_connect.types.timestamp.Timestamp"
    """<p>The timestamp for when the rule was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleSummary) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["RuleId"] = value["rule_id"]
    out["RuleArn"] = value["rule_arn"]
    import aws_sdk_connect.types.event_source_name

    out["EventSourceName"] = aws_sdk_connect.types.event_source_name.serialize_json(
        value["event_source_name"]
    )
    import aws_sdk_connect.types.rule_publish_status

    out["PublishStatus"] = aws_sdk_connect.types.rule_publish_status.serialize_json(
        value["publish_status"]
    )
    import aws_sdk_connect.types.action_summaries

    out["ActionSummaries"] = aws_sdk_connect.types.action_summaries.serialize_json(
        value["action_summaries"]
    )
    import aws_sdk_connect.types.timestamp

    out["CreatedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
        value["created_time"]
    )
    import aws_sdk_connect.types.timestamp

    out["LastUpdatedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
        value["last_updated_time"]
    )
    return out


def deserialize_json(data: dict) -> RuleSummary:
    out: RuleSummary = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("RuleSummary.name required")
    if "RuleId" in data:
        out["rule_id"] = data["RuleId"]
    else:
        raise DeserializationError("RuleSummary.rule_id required")
    if "RuleArn" in data:
        out["rule_arn"] = data["RuleArn"]
    else:
        raise DeserializationError("RuleSummary.rule_arn required")
    if "EventSourceName" in data:
        import aws_sdk_connect.types.event_source_name

        out["event_source_name"] = (
            aws_sdk_connect.types.event_source_name.deserialize_json(
                data["EventSourceName"]
            )
        )
    else:
        raise DeserializationError("RuleSummary.event_source_name required")
    if "PublishStatus" in data:
        import aws_sdk_connect.types.rule_publish_status

        out["publish_status"] = (
            aws_sdk_connect.types.rule_publish_status.deserialize_json(
                data["PublishStatus"]
            )
        )
    else:
        raise DeserializationError("RuleSummary.publish_status required")
    if "ActionSummaries" in data:
        import aws_sdk_connect.types.action_summaries

        out["action_summaries"] = (
            aws_sdk_connect.types.action_summaries.deserialize_json(
                data["ActionSummaries"]
            )
        )
    else:
        raise DeserializationError("RuleSummary.action_summaries required")
    if "CreatedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["created_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    else:
        raise DeserializationError("RuleSummary.created_time required")
    if "LastUpdatedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["last_updated_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    else:
        raise DeserializationError("RuleSummary.last_updated_time required")
    return out

"""Generated from Smithy shape ``com.amazonaws.connect#UpdateRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.rule_actions
    import aws_sdk_connect.types.rule_function
    import aws_sdk_connect.types.rule_id
    import aws_sdk_connect.types.rule_name
    import aws_sdk_connect.types.rule_publish_status


class UpdateRuleRequest(TypedDict):
    rule_id: "aws_sdk_connect.types.rule_id.RuleId"
    """<p>A unique identifier for the rule.</p>"""
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    name: "aws_sdk_connect.types.rule_name.RuleName"
    """<p>The name of the rule. You can change the name only if <code>TriggerEventSource</code> is one of the following values: <code>OnZendeskTicketCreate</code> | <code>OnZendeskTicketStatusUpdate</code> | <code>OnSalesforceCaseCreate</code> </p>"""
    function: "aws_sdk_connect.types.rule_function.RuleFunction"
    """<p>The conditions of the rule.</p>"""
    actions: "aws_sdk_connect.types.rule_actions.RuleActions"
    """<p>A list of actions to be run when the rule is triggered.</p>"""
    publish_status: "aws_sdk_connect.types.rule_publish_status.RulePublishStatus"
    """<p>The publish status of the rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRuleRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Function"] = value["function"]
    import aws_sdk_connect.types.rule_actions

    out["Actions"] = aws_sdk_connect.types.rule_actions.serialize_json(value["actions"])
    import aws_sdk_connect.types.rule_publish_status

    out["PublishStatus"] = aws_sdk_connect.types.rule_publish_status.serialize_json(
        value["publish_status"]
    )
    return out


def deserialize_json(data: dict) -> UpdateRuleRequest:
    out: UpdateRuleRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateRuleRequest.name required")
    if "Function" in data:
        out["function"] = data["Function"]
    else:
        raise DeserializationError("UpdateRuleRequest.function required")
    if "Actions" in data:
        import aws_sdk_connect.types.rule_actions

        out["actions"] = aws_sdk_connect.types.rule_actions.deserialize_json(
            data["Actions"]
        )
    else:
        raise DeserializationError("UpdateRuleRequest.actions required")
    if "PublishStatus" in data:
        import aws_sdk_connect.types.rule_publish_status

        out["publish_status"] = (
            aws_sdk_connect.types.rule_publish_status.deserialize_json(
                data["PublishStatus"]
            )
        )
    else:
        raise DeserializationError("UpdateRuleRequest.publish_status required")
    return out

"""Generated from Smithy shape ``com.amazonaws.connect#CreateRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.client_token
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.rule_actions
    import aws_sdk_connect.types.rule_function
    import aws_sdk_connect.types.rule_name
    import aws_sdk_connect.types.rule_publish_status
    import aws_sdk_connect.types.rule_trigger_event_source


class CreateRuleRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    name: "aws_sdk_connect.types.rule_name.RuleName"
    """<p>A unique name for the rule.</p>"""
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
    client_token: NotRequired["aws_sdk_connect.types.client_token.ClientToken"]
    r"""<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRuleRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
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
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateRuleRequest:
    out: CreateRuleRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateRuleRequest.name required")
    if "TriggerEventSource" in data:
        import aws_sdk_connect.types.rule_trigger_event_source

        out["trigger_event_source"] = (
            aws_sdk_connect.types.rule_trigger_event_source.deserialize_json(
                data["TriggerEventSource"]
            )
        )
    else:
        raise DeserializationError("CreateRuleRequest.trigger_event_source required")
    if "Function" in data:
        out["function"] = data["Function"]
    else:
        raise DeserializationError("CreateRuleRequest.function required")
    if "Actions" in data:
        import aws_sdk_connect.types.rule_actions

        out["actions"] = aws_sdk_connect.types.rule_actions.deserialize_json(
            data["Actions"]
        )
    else:
        raise DeserializationError("CreateRuleRequest.actions required")
    if "PublishStatus" in data:
        import aws_sdk_connect.types.rule_publish_status

        out["publish_status"] = (
            aws_sdk_connect.types.rule_publish_status.deserialize_json(
                data["PublishStatus"]
            )
        )
    else:
        raise DeserializationError("CreateRuleRequest.publish_status required")
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out

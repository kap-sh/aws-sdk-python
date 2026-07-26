"""Generated from Smithy shape ``com.amazonaws.connect#CreateRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.client_token
    import capo_connect.types.instance_id
    import capo_connect.types.rule_actions
    import capo_connect.types.rule_function
    import capo_connect.types.rule_name
    import capo_connect.types.rule_publish_status
    import capo_connect.types.rule_trigger_event_source


class CreateRuleRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    name: "capo_connect.types.rule_name.RuleName"
    """<p>A unique name for the rule.</p>"""
    trigger_event_source: (
        "capo_connect.types.rule_trigger_event_source.RuleTriggerEventSource"
    )
    """<p>The event source to trigger the rule.</p>"""
    function: "capo_connect.types.rule_function.RuleFunction"
    """<p>The conditions of the rule.</p>"""
    actions: "capo_connect.types.rule_actions.RuleActions"
    """<p>A list of actions to be run when the rule is triggered.</p>"""
    publish_status: "capo_connect.types.rule_publish_status.RulePublishStatus"
    """<p>The publish status of the rule.</p>"""
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    r"""<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRuleRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_connect.types.rule_trigger_event_source

    out["TriggerEventSource"] = (
        capo_connect.types.rule_trigger_event_source.serialize_json(
            value["trigger_event_source"]
        )
    )
    out["Function"] = value["function"]
    import capo_connect.types.rule_actions

    out["Actions"] = capo_connect.types.rule_actions.serialize_json(value["actions"])
    import capo_connect.types.rule_publish_status

    out["PublishStatus"] = capo_connect.types.rule_publish_status.serialize_json(
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
        import capo_connect.types.rule_trigger_event_source

        out["trigger_event_source"] = (
            capo_connect.types.rule_trigger_event_source.deserialize_json(
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
        import capo_connect.types.rule_actions

        out["actions"] = capo_connect.types.rule_actions.deserialize_json(
            data["Actions"]
        )
    else:
        raise DeserializationError("CreateRuleRequest.actions required")
    if "PublishStatus" in data:
        import capo_connect.types.rule_publish_status

        out["publish_status"] = capo_connect.types.rule_publish_status.deserialize_json(
            data["PublishStatus"]
        )
    else:
        raise DeserializationError("CreateRuleRequest.publish_status required")
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out

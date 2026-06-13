"""Generated from Smithy shape ``com.amazonaws.rtbfabric#CreateLinkRoutingRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.gateway_id
    import aws_sdk_rtbfabric.types.link_id
    import aws_sdk_rtbfabric.types.rule_condition
    import aws_sdk_rtbfabric.types.rule_priority
    import aws_sdk_rtbfabric.types.tags_map


class CreateLinkRoutingRuleRequest(TypedDict):
    client_token: "str"
    """<p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href=\"https://wikipedia.org/wiki/Universally_unique_identifier\">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>"""
    gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    link_id: "aws_sdk_rtbfabric.types.link_id.LinkId"
    """<p>The unique identifier of the link.</p>"""
    priority: "aws_sdk_rtbfabric.types.rule_priority.RulePriority"
    """<p>The priority of the routing rule. Lower numbers are evaluated first. Valid values are 1 to 1000. Priority must be unique among non-deleted rules within a link.</p>"""
    conditions: "aws_sdk_rtbfabric.types.rule_condition.RuleCondition"
    """<p>The conditions for the routing rule. All specified fields must match for the rule to apply. At least one condition field must be set.</p>"""
    tags: NotRequired["aws_sdk_rtbfabric.types.tags_map.TagsMap"]
    """<p>A map of the key-value pairs of the tag or tags to assign to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLinkRoutingRuleRequest) -> dict:
    out: dict = {}
    out["clientToken"] = value["client_token"]
    out["priority"] = value["priority"]
    import aws_sdk_rtbfabric.types.rule_condition

    out["conditions"] = aws_sdk_rtbfabric.types.rule_condition.serialize_json(
        value["conditions"]
    )
    if "tags" in value:
        import aws_sdk_rtbfabric.types.tags_map

        out["tags"] = aws_sdk_rtbfabric.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateLinkRoutingRuleRequest:
    out: CreateLinkRoutingRuleRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("CreateLinkRoutingRuleRequest.client_token required")
    if "priority" in data:
        out["priority"] = data["priority"]
    else:
        raise DeserializationError("CreateLinkRoutingRuleRequest.priority required")
    if "conditions" in data:
        import aws_sdk_rtbfabric.types.rule_condition

        out["conditions"] = aws_sdk_rtbfabric.types.rule_condition.deserialize_json(
            data["conditions"]
        )
    else:
        raise DeserializationError("CreateLinkRoutingRuleRequest.conditions required")
    if "tags" in data:
        import aws_sdk_rtbfabric.types.tags_map

        out["tags"] = aws_sdk_rtbfabric.types.tags_map.deserialize_json(data["tags"])
    return out

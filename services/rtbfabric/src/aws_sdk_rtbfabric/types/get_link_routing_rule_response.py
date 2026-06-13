"""Generated from Smithy shape ``com.amazonaws.rtbfabric#GetLinkRoutingRuleResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_rtbfabric.types.gateway_id
    import aws_sdk_rtbfabric.types.link_id
    import aws_sdk_rtbfabric.types.rule_condition
    import aws_sdk_rtbfabric.types.rule_id
    import aws_sdk_rtbfabric.types.rule_priority
    import aws_sdk_rtbfabric.types.rule_status
    import aws_sdk_rtbfabric.types.tags_map


class GetLinkRoutingRuleResponse(TypedDict):
    gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    link_id: "aws_sdk_rtbfabric.types.link_id.LinkId"
    """<p>The unique identifier of the link.</p>"""
    rule_id: "aws_sdk_rtbfabric.types.rule_id.RuleId"
    """<p>The unique identifier of the routing rule.</p>"""
    priority: "aws_sdk_rtbfabric.types.rule_priority.RulePriority"
    """<p>The priority of the routing rule.</p>"""
    conditions: "aws_sdk_rtbfabric.types.rule_condition.RuleCondition"
    """<p>The conditions for the routing rule.</p>"""
    status: "aws_sdk_rtbfabric.types.rule_status.RuleStatus"
    """<p>The status of the routing rule.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp of when the routing rule was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp of when the routing rule was last updated.</p>"""
    tags: NotRequired["aws_sdk_rtbfabric.types.tags_map.TagsMap"]
    """<p>A map of the key-value pairs for the tag or tags assigned to the specified resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLinkRoutingRuleResponse) -> dict:
    out: dict = {}
    out["gatewayId"] = value["gateway_id"]
    out["linkId"] = value["link_id"]
    out["ruleId"] = value["rule_id"]
    out["priority"] = value["priority"]
    import aws_sdk_rtbfabric.types.rule_condition

    out["conditions"] = aws_sdk_rtbfabric.types.rule_condition.serialize_json(
        value["conditions"]
    )
    import aws_sdk_rtbfabric.types.rule_status

    out["status"] = aws_sdk_rtbfabric.types.rule_status.serialize_json(value["status"])
    import aws_sdk_rtbfabric.types._prelude.timestamp

    out["createdAt"] = aws_sdk_rtbfabric.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_rtbfabric.types._prelude.timestamp

    out["updatedAt"] = aws_sdk_rtbfabric.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    if "tags" in value:
        import aws_sdk_rtbfabric.types.tags_map

        out["tags"] = aws_sdk_rtbfabric.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetLinkRoutingRuleResponse:
    out: GetLinkRoutingRuleResponse = {}  # type: ignore[typeddict-item]
    if "gatewayId" in data:
        out["gateway_id"] = data["gatewayId"]
    else:
        raise DeserializationError("GetLinkRoutingRuleResponse.gateway_id required")
    if "linkId" in data:
        out["link_id"] = data["linkId"]
    else:
        raise DeserializationError("GetLinkRoutingRuleResponse.link_id required")
    if "ruleId" in data:
        out["rule_id"] = data["ruleId"]
    else:
        raise DeserializationError("GetLinkRoutingRuleResponse.rule_id required")
    if "priority" in data:
        out["priority"] = data["priority"]
    else:
        raise DeserializationError("GetLinkRoutingRuleResponse.priority required")
    if "conditions" in data:
        import aws_sdk_rtbfabric.types.rule_condition

        out["conditions"] = aws_sdk_rtbfabric.types.rule_condition.deserialize_json(
            data["conditions"]
        )
    else:
        raise DeserializationError("GetLinkRoutingRuleResponse.conditions required")
    if "status" in data:
        import aws_sdk_rtbfabric.types.rule_status

        out["status"] = aws_sdk_rtbfabric.types.rule_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GetLinkRoutingRuleResponse.status required")
    if "createdAt" in data:
        import aws_sdk_rtbfabric.types._prelude.timestamp

        out["created_at"] = aws_sdk_rtbfabric.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("GetLinkRoutingRuleResponse.created_at required")
    if "updatedAt" in data:
        import aws_sdk_rtbfabric.types._prelude.timestamp

        out["updated_at"] = aws_sdk_rtbfabric.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("GetLinkRoutingRuleResponse.updated_at required")
    if "tags" in data:
        import aws_sdk_rtbfabric.types.tags_map

        out["tags"] = aws_sdk_rtbfabric.types.tags_map.deserialize_json(data["tags"])
    return out

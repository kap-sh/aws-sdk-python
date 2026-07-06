"""Generated from Smithy shape ``com.amazonaws.rtbfabric#LinkRoutingRuleSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_rtbfabric.types.rule_condition
    import aws_sdk_rtbfabric.types.rule_id
    import aws_sdk_rtbfabric.types.rule_priority
    import aws_sdk_rtbfabric.types.rule_status


class LinkRoutingRuleSummary(TypedDict, closed=True):
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


# --- restJson1 ser/de ---
def serialize_json(value: LinkRoutingRuleSummary) -> dict:
    out: dict = {}
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
    return out


def deserialize_json(data: dict) -> LinkRoutingRuleSummary:
    out: LinkRoutingRuleSummary = {}  # type: ignore[typeddict-item]
    if "ruleId" in data:
        out["rule_id"] = data["ruleId"]
    else:
        raise DeserializationError("LinkRoutingRuleSummary.rule_id required")
    if "priority" in data:
        out["priority"] = data["priority"]
    else:
        raise DeserializationError("LinkRoutingRuleSummary.priority required")
    if "conditions" in data:
        import aws_sdk_rtbfabric.types.rule_condition

        out["conditions"] = aws_sdk_rtbfabric.types.rule_condition.deserialize_json(
            data["conditions"]
        )
    else:
        raise DeserializationError("LinkRoutingRuleSummary.conditions required")
    if "status" in data:
        import aws_sdk_rtbfabric.types.rule_status

        out["status"] = aws_sdk_rtbfabric.types.rule_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("LinkRoutingRuleSummary.status required")
    if "createdAt" in data:
        import aws_sdk_rtbfabric.types._prelude.timestamp

        out["created_at"] = aws_sdk_rtbfabric.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("LinkRoutingRuleSummary.created_at required")
    if "updatedAt" in data:
        import aws_sdk_rtbfabric.types._prelude.timestamp

        out["updated_at"] = aws_sdk_rtbfabric.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("LinkRoutingRuleSummary.updated_at required")
    return out

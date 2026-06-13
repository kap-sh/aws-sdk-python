"""Generated from Smithy shape ``com.amazonaws.rtbfabric#UpdateLinkRoutingRuleResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_rtbfabric.types.rule_id
    import aws_sdk_rtbfabric.types.rule_status


class UpdateLinkRoutingRuleResponse(TypedDict):
    rule_id: "aws_sdk_rtbfabric.types.rule_id.RuleId"
    """<p>The unique identifier of the routing rule.</p>"""
    status: "aws_sdk_rtbfabric.types.rule_status.RuleStatus"
    """<p>The status of the routing rule.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp of when the routing rule was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLinkRoutingRuleResponse) -> dict:
    out: dict = {}
    out["ruleId"] = value["rule_id"]
    import aws_sdk_rtbfabric.types.rule_status

    out["status"] = aws_sdk_rtbfabric.types.rule_status.serialize_json(value["status"])
    import aws_sdk_rtbfabric.types._prelude.timestamp

    out["updatedAt"] = aws_sdk_rtbfabric.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> UpdateLinkRoutingRuleResponse:
    out: UpdateLinkRoutingRuleResponse = {}  # type: ignore[typeddict-item]
    if "ruleId" in data:
        out["rule_id"] = data["ruleId"]
    else:
        raise DeserializationError("UpdateLinkRoutingRuleResponse.rule_id required")
    if "status" in data:
        import aws_sdk_rtbfabric.types.rule_status

        out["status"] = aws_sdk_rtbfabric.types.rule_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("UpdateLinkRoutingRuleResponse.status required")
    if "updatedAt" in data:
        import aws_sdk_rtbfabric.types._prelude.timestamp

        out["updated_at"] = aws_sdk_rtbfabric.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("UpdateLinkRoutingRuleResponse.updated_at required")
    return out

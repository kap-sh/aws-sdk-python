"""Generated from Smithy shape ``com.amazonaws.rtbfabric#CreateLinkRoutingRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_rtbfabric.types.rule_id
    import aws_sdk_rtbfabric.types.rule_status


class CreateLinkRoutingRuleResponse(TypedDict, closed=True):
    rule_id: "aws_sdk_rtbfabric.types.rule_id.RuleId"
    """<p>The unique identifier of the routing rule.</p>"""
    status: "aws_sdk_rtbfabric.types.rule_status.RuleStatus"
    """<p>The status of the routing rule.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp of when the routing rule was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLinkRoutingRuleResponse) -> dict:
    out: dict = {}
    out["ruleId"] = value["rule_id"]
    import aws_sdk_rtbfabric.types.rule_status

    out["status"] = aws_sdk_rtbfabric.types.rule_status.serialize_json(value["status"])
    import aws_sdk_rtbfabric.types._prelude.timestamp

    out["createdAt"] = aws_sdk_rtbfabric.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    return out


def deserialize_json(data: dict) -> CreateLinkRoutingRuleResponse:
    out: CreateLinkRoutingRuleResponse = {}  # type: ignore[typeddict-item]
    if "ruleId" in data:
        out["rule_id"] = data["ruleId"]
    else:
        raise DeserializationError("CreateLinkRoutingRuleResponse.rule_id required")
    if "status" in data:
        import aws_sdk_rtbfabric.types.rule_status

        out["status"] = aws_sdk_rtbfabric.types.rule_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("CreateLinkRoutingRuleResponse.status required")
    if "createdAt" in data:
        import aws_sdk_rtbfabric.types._prelude.timestamp

        out["created_at"] = aws_sdk_rtbfabric.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("CreateLinkRoutingRuleResponse.created_at required")
    return out

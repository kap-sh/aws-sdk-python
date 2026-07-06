"""Generated from Smithy shape ``com.amazonaws.rtbfabric#DeleteLinkRoutingRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.rule_id
    import aws_sdk_rtbfabric.types.rule_status


class DeleteLinkRoutingRuleResponse(TypedDict, closed=True):
    rule_id: "aws_sdk_rtbfabric.types.rule_id.RuleId"
    """<p>The unique identifier of the routing rule.</p>"""
    status: "aws_sdk_rtbfabric.types.rule_status.RuleStatus"
    """<p>The status of the routing rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteLinkRoutingRuleResponse) -> dict:
    out: dict = {}
    out["ruleId"] = value["rule_id"]
    import aws_sdk_rtbfabric.types.rule_status

    out["status"] = aws_sdk_rtbfabric.types.rule_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> DeleteLinkRoutingRuleResponse:
    out: DeleteLinkRoutingRuleResponse = {}  # type: ignore[typeddict-item]
    if "ruleId" in data:
        out["rule_id"] = data["ruleId"]
    else:
        raise DeserializationError("DeleteLinkRoutingRuleResponse.rule_id required")
    if "status" in data:
        import aws_sdk_rtbfabric.types.rule_status

        out["status"] = aws_sdk_rtbfabric.types.rule_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("DeleteLinkRoutingRuleResponse.status required")
    return out

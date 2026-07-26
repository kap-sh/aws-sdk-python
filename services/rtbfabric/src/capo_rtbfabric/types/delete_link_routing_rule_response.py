"""Generated from Smithy shape ``com.amazonaws.rtbfabric#DeleteLinkRoutingRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rtbfabric.types.rule_id
    import capo_rtbfabric.types.rule_status


class DeleteLinkRoutingRuleResponse(TypedDict, closed=True):
    rule_id: "capo_rtbfabric.types.rule_id.RuleId"
    """<p>The unique identifier of the routing rule.</p>"""
    status: "capo_rtbfabric.types.rule_status.RuleStatus"
    """<p>The status of the routing rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteLinkRoutingRuleResponse) -> dict:
    out: dict = {}
    out["ruleId"] = value["rule_id"]
    import capo_rtbfabric.types.rule_status

    out["status"] = capo_rtbfabric.types.rule_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> DeleteLinkRoutingRuleResponse:
    out: DeleteLinkRoutingRuleResponse = {}  # type: ignore[typeddict-item]
    if "ruleId" in data:
        out["rule_id"] = data["ruleId"]
    else:
        raise DeserializationError("DeleteLinkRoutingRuleResponse.rule_id required")
    if "status" in data:
        import capo_rtbfabric.types.rule_status

        out["status"] = capo_rtbfabric.types.rule_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("DeleteLinkRoutingRuleResponse.status required")
    return out

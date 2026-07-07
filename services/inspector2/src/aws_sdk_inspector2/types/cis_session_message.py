"""Generated from Smithy shape ``com.amazonaws.inspector2#CisSessionMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.cis_rule_details
    import aws_sdk_inspector2.types.cis_rule_status
    import aws_sdk_inspector2.types.rule_id


class CisSessionMessage(TypedDict, closed=True):
    rule_id: "aws_sdk_inspector2.types.rule_id.RuleId"
    """<p>The rule ID for the CIS session message.</p>"""
    status: "aws_sdk_inspector2.types.cis_rule_status.CisRuleStatus"
    """<p>The status of the CIS session message.</p>"""
    cis_rule_details: "aws_sdk_inspector2.types.cis_rule_details.CisRuleDetails"
    """<p>The CIS rule details for the CIS session message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CisSessionMessage) -> dict:
    out: dict = {}
    out["ruleId"] = value["rule_id"]
    import aws_sdk_inspector2.types.cis_rule_status

    out["status"] = aws_sdk_inspector2.types.cis_rule_status.serialize_json(
        value["status"]
    )
    import aws_sdk_inspector2.types.cis_rule_details

    out["cisRuleDetails"] = aws_sdk_inspector2.types.cis_rule_details.serialize_json(
        value["cis_rule_details"]
    )
    return out


def deserialize_json(data: dict) -> CisSessionMessage:
    out: CisSessionMessage = {}  # type: ignore[typeddict-item]
    if "ruleId" in data:
        out["rule_id"] = data["ruleId"]
    else:
        raise DeserializationError("CisSessionMessage.rule_id required")
    if "status" in data:
        import aws_sdk_inspector2.types.cis_rule_status

        out["status"] = aws_sdk_inspector2.types.cis_rule_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("CisSessionMessage.status required")
    if "cisRuleDetails" in data:
        import aws_sdk_inspector2.types.cis_rule_details

        out["cis_rule_details"] = (
            aws_sdk_inspector2.types.cis_rule_details.deserialize_json(
                data["cisRuleDetails"]
            )
        )
    else:
        raise DeserializationError("CisSessionMessage.cis_rule_details required")
    return out

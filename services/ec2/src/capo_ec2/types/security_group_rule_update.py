"""Generated from Smithy shape ``com.amazonaws.ec2#SecurityGroupRuleUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.security_group_rule_id
    import capo_ec2.types.security_group_rule_request


class SecurityGroupRuleUpdate(TypedDict, closed=True):
    security_group_rule_id: NotRequired[
        "capo_ec2.types.security_group_rule_id.SecurityGroupRuleId"
    ]
    """<p>The ID of the security group rule.</p>"""
    security_group_rule: NotRequired[
        "capo_ec2.types.security_group_rule_request.SecurityGroupRuleRequest"
    ]
    """<p>Information about the security group rule.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SecurityGroupRuleUpdate, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "security_group_rule_id" in value:
        pairs.append(
            (f"{prefix}.SecurityGroupRuleId", str(value["security_group_rule_id"]))
        )
    if "security_group_rule" in value:
        import capo_ec2.types.security_group_rule_request

        capo_ec2.types.security_group_rule_request.serialize_ec2_query(
            value["security_group_rule"], pairs, f"{prefix}.SecurityGroupRule"
        )


def deserialize_ec2_query(el: Element) -> SecurityGroupRuleUpdate:
    out: SecurityGroupRuleUpdate = {}  # type: ignore[typeddict-item]
    child_security_group_rule_id = el.find("SecurityGroupRuleId")
    if child_security_group_rule_id is not None:
        out["security_group_rule_id"] = str(child_security_group_rule_id.text or "")
    child_security_group_rule = el.find("SecurityGroupRule")
    if child_security_group_rule is not None:
        import capo_ec2.types.security_group_rule_request

        out["security_group_rule"] = (
            capo_ec2.types.security_group_rule_request.deserialize_ec2_query(
                child_security_group_rule
            )
        )
    return out
